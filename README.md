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
- https://medium.com/@cstroliadavis/building-mcp-servers-536969d27809#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyMWYzYmM2NmYwNzUxZjc4NDA2MDY3OTliMWFkZjllOWZiNjBkZmIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTA0ODc0NjQzMjYxOTgyNzM0MjkiLCJlbWFpbCI6ImxvdWthamNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5iZiI6MTc0MzUzMjczNSwibmFtZSI6IkxvdWthIEphY3F1ZXMtQ2hldmFsbGllciAoTGFsdWthKSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLd2dvNDRTYXhFeHYzQ1FqaC0xVV9kSzdEa0pPQUxkRy1LZU5xN05VLUtMeEh4d1lzcD1zOTYtYyIsImdpdmVuX25hbWUiOiJMb3VrYSIsImZhbWlseV9uYW1lIjoiSmFjcXVlcy1DaGV2YWxsaWVyIiwiaWF0IjoxNzQzNTMzMDM1LCJleHAiOjE3NDM1MzY2MzUsImp0aSI6ImVjZWEwNzc1ZjJiMDlhYTExYjZhZTAwNGE4NmY0MDA5YzIzOGUxZDcifQ.JQgF7Fon3ZPXtAfiWP_mvm-bpa8e6b2uazWxjGpcrZIGyflL4umateXCRk1ql2lvMirxOjcPbYoYL2mbBKT-KgxNDwQyfiQQBaOXDOz_VwhKDwiZ8jF8Su74LCE-52yA9VGXZjdT9hKfpps2RPWOaVsu_DNuEXnr3y1xDO9XHxenwwZMTBthzh3mUUjeUvSDKZu66wRBql7QWxZYxeMpDDK2TDDtGlD1nEKQ3QOozWMjAp6n4ZYaLmBxPEynk4I8U33lozUR-syHonVGjHKlRrvQCad0FEYcfu5shEzixofHC_RLKl1mjuW0wmNdYzZSrhLdTo_5OqKi2T8VX-JcdA
- https://modelcontextprotocol.io/introduction
- https://www.librechat.ai/
- https://github.com/cline/cline
- https://doomerhunter.fr/
