import asyncio
import subprocess
from typing import Optional

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
            name="run-command",
            description="Execute a shell command and return its output",
            inputSchema={
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The shell command to execute",
                    },
                    "cwd": {
                        "type": "string",
                        "description": "Working directory for the command (optional)",
                    },
                },
                "required": ["command"],
            },
        )
    ]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """
    Handle tool execution requests.
    Tools can modify server state and notify clients of changes.
    """
    if name != "run-command":
        raise ValueError(f"Unknown tool: {name}")

    if not arguments:
        raise ValueError("Missing arguments")

    command = arguments.get("command")
    cwd = arguments.get("cwd", "/tmp")

    if not command:
        raise ValueError("Missing command")

    try:
        # Run the command with shell=True for bash interpolation
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=cwd,
        )

        stdout, stderr = process.communicate()

        # Prepare the response
        response_parts = []

        if stdout:
            response_parts.append(f"stdout:\n{stdout}")
        if stderr:
            response_parts.append(f"stderr:\n{stderr}")
        if not stdout and not stderr:
            response_parts.append("Command executed successfully with no output")

        return [
            types.TextContent(
                type="text",
                text="\n".join(response_parts),
            )
        ]

    except Exception as e:
        return [
            types.TextContent(
                type="text",
                text=f"Error executing command: {str(e)}",
            )
        ]


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
