[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/czirakim-f5-mcp-server-badge.png)](https://mseep.ai/app/czirakim-f5-mcp-server)

# F5 MCP Server
[![smithery badge](https://smithery.ai/badge/@czirakim/F5.MCP.server)](https://smithery.ai/server/@czirakim/F5.MCP.server)

<img width="724" alt="image" src="https://github.com/user-attachments/assets/6bffb811-3e89-49fb-9d31-c7173afc9adc" />

This project is a **MCP( Model Context Protocol ) server** designed to interact with F5 devices using the **iControl REST API**. It provides a set of tools to manage F5 objects such as virtual servers (VIPs), pools, iRules, and profiles. The server is implemented using the `FastMCP` framework and exposes functionalities for creating, updating, listing, and deleting F5 objects.

## Features

- **Tool-Based API**: The project defines tools (`list_tool`, `create_tool`, `update_tool`, `delete_tool`) that encapsulate operations on F5 devices.
- **REST API Integration**: Uses Python's `requests` library to communicate with F5 devices via the iControl REST API.
- **Environment Configuration**: Sensitive information like IP addresses and authorization strings are managed through environment variables loaded from a `.env` file.
- **Extensibility**: Modular design allows additional tools or functionalities to be added easily.
- **Transport Support**: The server runs using the `stdio` transport, making it compatible with various client integrations.
- **Dockerfile**: If you want to run this as a Docker container

### Key Files

- **`F5MCPserver.py`**: The main server file that initializes the MCP server and defines the tools.
- **`Tools/F5object.py`**: A utility class for performing CRUD operations on F5 objects.

The repo also contains an example of the Claude desktop app config file.
Only `F5object.py` is used from the Tools folder. The others were used in development.

### `It was tested with the Claude Desktop app. The MCP server was hosted in Windows WSL.`


<img width="362" alt="image" src="https://github.com/user-attachments/assets/06ac07e0-2ab7-4675-8c7b-c3809bc364ad" />

### Installing via Smithery

To install F5 Device Management Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@czirakim/F5.MCP.server):

```bash
npx -y @smithery/cli install @czirakim/F5.MCP.server --client claude
```


### Credits
This was written by Mihai Cziraki
