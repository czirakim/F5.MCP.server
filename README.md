# F5 MCP Server

This project is a **Multi-Channel Protocol (MCP) server** designed to interact with F5 devices using the **iControl REST API**. It provides a set of tools to manage F5 objects such as virtual servers (VIPs), pools, iRules, and profiles. The server is implemented using the `FastMCP` framework and exposes functionalities for creating, updating, listing, and deleting F5 objects.

## Features

- **Tool-Based API**: The project defines tools (`list_tool`, `create_tool`, `update_tool`, `delete_tool`) that encapsulate operations on F5 devices.
- **REST API Integration**: Uses Python's `requests` library to communicate with F5 devices via the iControl REST API.
- **Environment Configuration**: Sensitive information like IP addresses and authorization strings are managed through environment variables loaded from a `.env` file.
- **Extensibility**: Modular design allows additional tools or functionalities to be added easily.
- **Transport Support**: The server runs using the `stdio` transport, making it compatible with various client integrations.

### Key Files

- **`F5MCPserver.py`**: The main server file that initializes the MCP server and defines the tools.
- **`Tools/F5object.py`**: A utility class for performing CRUD operations on F5 objects.

### Credits
This was written by Mihai Cziraki



