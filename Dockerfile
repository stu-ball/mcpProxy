# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app

# Install FastMCP v3 (latest release candidate)
RUN pip install --no-cache-dir fastmcp==3.0.0rc2

COPY proxy_server.py ./

EXPOSE 8490

CMD ["python", "proxy_server.py"]
