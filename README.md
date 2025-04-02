# mcpoc MCP server

Below are our dirty notes for a quick PoC creating a MCP server for automated binary to assembly to C code.

Blasting our `AuTo DeCoMpIlEr Ai BaZeD`! 😎

If you want to know how to use this badly documented PoC!

[![OffenSkill LiveStream](https://img.youtube.com/vi/FHdkypBj9Bw/0.jpg)](https://www.youtube.com/watch?v=FHdkypBj9Bw)


## Setup & Test

```bash
mise install
gcc challenge.c -o /tmp/challenge
npm install -g @anthropic-ai/claude-code
claude code # Setup
claude mcp add # Follow instructions, mcp cmd is "uv --directory /home/lalu/mcpoc/mcpoc run mcpoc"
claude code # Interact with your mcp!
# Prompt: Reverse the source code of /tmp/challenge
```

## Debug

Upon launching, the Inspector will display a URL that you can access in your browser to begin debugging.

```bash
npx @modelcontextprotocol/inspector uv --directory /home/lalu/mcpoc/mcpoc run mcpoc
```

## Links used during the livestream

- https://github.com/evalstate/fast-agent
- https://claude.ai/download
- https://apidog.com/blog/cline-mcp-servers/
- https://medium.com/@cstroliadavis/building-mcp-servers-536969d27809
- https://github.com/modelcontextprotocol/create-python-server
- https://github.com/modelcontextprotocol/inspector
- https://modelcontextprotocol.io/clients
- https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview
- https://docs.anthropic.com/en/docs/agents-and-tools/mcp?q=mcp
- https://medium.com/@cstroliadavis/building-mcp-servers-536969d27809
- https://modelcontextprotocol.io/introduction
- https://www.librechat.ai/
- https://github.com/cline/cline
- https://doomerhunter.fr/
