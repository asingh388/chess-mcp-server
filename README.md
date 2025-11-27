Install this MCP Server by adding the following JSON code to your json config file
```JSON
{
  "mcpServers": {
    "chess": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/asingh388/chess-mcp-server.git"
        "chess"
      ]
    }
  }
}
```