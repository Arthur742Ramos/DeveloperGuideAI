#!/usr/bin/env python3
"""
Documentation Search MCP Server

A simple MCP server that searches markdown documentation files.
Demonstrates core MCP patterns from Chapter 18.

Usage:
    python doc_search_server.py

Environment:
    DOCS_PATH - Path to documentation directory (default: ./docs)
"""

import os
import re
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Initialize server
server = Server("doc-search")

# Configuration
DOCS_PATH = Path(os.environ.get("DOCS_PATH", "./docs"))


def index_documents() -> dict[str, str]:
    """Index all markdown files in DOCS_PATH."""
    index = {}
    if not DOCS_PATH.exists():
        return index

    for md_file in DOCS_PATH.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            relative_path = str(md_file.relative_to(DOCS_PATH))
            index[relative_path] = content
        except Exception:
            continue

    return index


def search_content(query: str, content: str) -> list[str]:
    """Find lines matching query in content."""
    matches = []
    query_lower = query.lower()

    for i, line in enumerate(content.split("\n"), 1):
        if query_lower in line.lower():
            matches.append(f"Line {i}: {line.strip()}")

    return matches


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="search_docs",
            description="Search documentation for a query string. Returns matching files and lines.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Text to search for in documentation"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="list_docs",
            description="List all available documentation files.",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="read_doc",
            description="Read the full content of a specific documentation file.",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Relative path to the documentation file"
                    }
                },
                "required": ["path"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""

    if name == "search_docs":
        query = arguments.get("query", "")
        if not query:
            return [TextContent(type="text", text="Error: query is required")]

        index = index_documents()
        if not index:
            return [TextContent(type="text", text=f"No documents found in {DOCS_PATH}")]

        results = []
        for path, content in index.items():
            matches = search_content(query, content)
            if matches:
                results.append(f"\n## {path}\n" + "\n".join(matches[:5]))  # Limit matches per file

        if not results:
            return [TextContent(type="text", text=f"No matches found for: {query}")]

        return [TextContent(type="text", text=f"Found matches in {len(results)} file(s):" + "".join(results))]

    elif name == "list_docs":
        index = index_documents()
        if not index:
            return [TextContent(type="text", text=f"No documents found in {DOCS_PATH}")]

        file_list = "\n".join(f"- {path}" for path in sorted(index.keys()))
        return [TextContent(type="text", text=f"Documentation files:\n{file_list}")]

    elif name == "read_doc":
        path = arguments.get("path", "")
        if not path:
            return [TextContent(type="text", text="Error: path is required")]

        full_path = DOCS_PATH / path

        # Security: prevent path traversal
        try:
            full_path = full_path.resolve()
            if not str(full_path).startswith(str(DOCS_PATH.resolve())):
                return [TextContent(type="text", text="Error: path outside docs directory")]
        except Exception:
            return [TextContent(type="text", text="Error: invalid path")]

        if not full_path.exists():
            return [TextContent(type="text", text=f"Error: file not found: {path}")]

        try:
            content = full_path.read_text(encoding="utf-8")
            return [TextContent(type="text", text=content)]
        except Exception as e:
            return [TextContent(type="text", text=f"Error reading file: {e}")]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    """Run the server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
