# FastMCP v3 Proxy (Single Docker Container)

## Overview
This project implements a FastMCP v3 Proxy server in a single Docker container. The proxy exposes a unified MCP API at `http://localhost:8490/mcp` using the streamable-http protocol. It demonstrates how to aggregate multiple MCP servers (including a local example server) and make them accessible through a single endpoint, suitable for integration with any MCP-compliant tool or client.

- **Proxy Port:** 8490 (only port used)
- **MCP Endpoint:** `http://localhost:8490/mcp`
- **Dockerized:** Yes (single container)
- **FastMCP Version:** 3.0.0rc2

## Features
- **Proxy Provider:** Aggregates and exposes one or more MCP servers behind a single endpoint.
- **Example MCP Server:** Included and mounted under the `example_` namespace.
- **Multiprocess:** Both the proxy and example server run in the same container using Python multiprocessing.
- **Streamable HTTP:** Fully compatible with FastMCP v3 streamable-http protocol.

## File Structure
- [`proxy_server.py`](proxy_server.py): Main entrypoint. Launches both the example server and the proxy.
- [`Dockerfile`](Dockerfile): Builds the container with FastMCP v3 and runs the proxy on port 8490.
- [`README.md`](README.md): This documentation.

## Usage

### 1. Build the Docker Image
```sh
docker build -t fastmcp-proxy .
```

### 2. Run the Container
```sh
docker run --rm -p 8490:8490 fastmcp-proxy
```

The proxy and example server will both start automatically.

### 3. MCP Endpoint
- The MCP API is available at: `http://localhost:8490/mcp`
- All tools from the example server are exposed with the prefix `example_` (e.g., `example_hello_world`).

## Example Tool
The included example MCP server exposes one tool:

- **Tool Name:** `example_hello_world`
- **Description:** Returns a hello message.
- **Invocation:** No input required.

## How to List and Call Tools

### Using the Official FastMCP CLI (Recommended)

#### List Tools
```sh
fastmcp list http://localhost:8490/mcp
```

#### Call the Example Tool
```sh
fastmcp call http://localhost:8490/mcp example_hello_world --json
```

**Expected Output:**
```json
{
  "result": "Hello from the example MCP server!"
}
```

### Why Raw HTTP Won't Work
FastMCP v3 streamable-http requires a session handshake protocol that is only handled by the official FastMCP client/CLI. Direct HTTP requests (e.g., with curl) will fail with `Missing session ID` errors. Always use the FastMCP client or compatible agent.

## How It Works
- The container launches the example server on port 8500 and the proxy on port 8490.
- The proxy mounts the example server using the `create_proxy` function and exposes its tools under the `example_` prefix.
- All MCP requests go through the proxy, which forwards them to the appropriate backend server(s).

## Extending
To add more MCP servers, modify `proxy_server.py` to launch additional servers and mount them in the proxy with unique prefixes.

## References
- [FastMCP v3 Documentation](https://gofastmcp.com/servers/providers/proxy)
- [Streamable HTTP Protocol](https://gofastmcp.com/v2/clients/transports)
- [FastMCP CLI Usage](https://github.com/jlowin/fastmcp/blob/main/skills/fastmcp-client-cli/SKILL.md)

---

**Maintainer:** Stuart Ball
