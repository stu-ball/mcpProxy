from fastmcp import FastMCP
from fastmcp.server import create_proxy
import multiprocessing
import time
import signal
import sys

# Example MCP server with a simple tool
def create_example_server():
    server = FastMCP("example")

    @server.tool
    def hello_world() -> str:
        """Returns a hello message."""
        return "Hello from the example MCP server!"

    return server

def run_example_server():
    example_server = create_example_server()
    example_server.run(transport="http", host="0.0.0.0", port=8500, path="/mcp")

if __name__ == "__main__":
    # Start the example server in a separate process
    p = multiprocessing.Process(target=run_example_server)
    p.start()
    time.sleep(2)  # Give the example server time to start

    try:
        # Create a proxy to the example server
        proxy = FastMCP("Proxy")
        proxy.mount(create_proxy("http://localhost:8500/mcp"), prefix="example")
        proxy.run(transport="http", host="0.0.0.0", port=8490, path="/mcp")
    except KeyboardInterrupt:
        pass
    finally:
        p.terminate()
        p.join()
        sys.exit(0)
