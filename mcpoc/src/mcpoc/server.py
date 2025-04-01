import asyncio
import subprocess
from typing import Optional
import os

from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
from pydantic import AnyUrl
import mcp.server.stdio

server = Server("mcpoc")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """
    List available tools.
    Each tool specifies its arguments using JSON Schema validation.
    """
    return [
        types.Tool(
            name="write",
            description="Write C code to /tmp/main.c",
            inputSchema={
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "The C code to write to /tmp/main.c",
                    },
                },
                "required": ["code"],
            },
        ),
        types.Tool(
            name="compile",
            description="Compile the C code in /tmp/main.c using gcc",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        types.Tool(
            name="disassembly",
            description="Generate disassembly of a binary using objdump",
            inputSchema={
                "type": "object",
                "properties": {
                    "binary": {
                        "type": "string",
                        "description": "Path to the binary to disassemble",
                    },
                },
                "required": ["binary"],
            },
        ),
    ]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """
    Handle tool execution requests.
    Tools can modify server state and notify clients of changes.
    """
    if not arguments:
        arguments = {}

    if name == "write":
        code = arguments.get("code")
        if not code:
            raise ValueError("Missing code")

        try:
            with open("/tmp/main.c", "w") as f:
                f.write(code)
            return [
                types.TextContent(
                    type="text",
                    text="Successfully wrote code to /tmp/main.c",
                )
            ]
        except Exception as e:
            return [
                types.TextContent(
                    type="text",
                    text=f"Error writing code: {str(e)}",
                )
            ]

    elif name == "compile":
        try:
            process = subprocess.Popen(
                ["gcc", "/tmp/main.c", "-o", "/tmp/main"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                return [
                    types.TextContent(
                        type="text",
                        text=f"Successfully compiled to /tmp/main",
                    )
                ]
            else:
                return [
                    types.TextContent(
                        type="text",
                        text=f"Compilation failed:\n{stderr}",
                    )
                ]
        except Exception as e:
            return [
                types.TextContent(
                    type="text",
                    text=f"Error during compilation: {str(e)}",
                )
            ]

    elif name == "disassembly":
        binary = arguments.get("binary")
        if not binary:
            raise ValueError("Missing binary path")

        if not os.path.exists(binary):
            return [
                types.TextContent(
                    type="text",
                    text=f"Error: Binary file {binary} does not exist",
                )
            ]

        try:
            process = subprocess.Popen(
                ["objdump", "-d", binary],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                return [
                    types.TextContent(
                        type="text",
                        text=stdout,
                    )
                ]
            else:
                return [
                    types.TextContent(
                        type="text",
                        text=f"Disassembly failed:\n{stderr}",
                    )
                ]
        except Exception as e:
            return [
                types.TextContent(
                    type="text",
                    text=f"Error during disassembly: {str(e)}",
                )
            ]

    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    # Run the server using stdin/stdout streams
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mcpoc",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
