# MCP Server Examples

Model Context Protocol (MCP) servers extend AI coding assistants with custom tools. These examples demonstrate common patterns.

## What is MCP?

MCP is a protocol that allows AI assistants (like Claude Code) to call external tools. Instead of describing what you want in natural language, you give the AI actual capabilities:

- Query your database
- Search your documentation
- Access internal APIs
- Run custom analysis

## Examples in This Directory

### Python Example (`python/`)
A documentation search server that indexes markdown files.

```bash
cd python
pip install -r requirements.txt
python doc_search_server.py
```

### TypeScript Example (`typescript/`)
A project metrics server that analyzes code statistics.

```bash
cd typescript
npm install
npm run build
npm start
```

## Adding to Claude Code

Add to your `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "doc-search": {
      "command": "python",
      "args": ["path/to/doc_search_server.py"],
      "env": {
        "DOCS_PATH": "/path/to/your/docs"
      }
    }
  }
}
```

## Tool Design Principles

From Chapter 18 of the book:

### 1. Single Responsibility
Each tool should do one thing well.

```python
# Good: Specific tool
@server.tool()
def search_docs(query: str) -> list[str]:
    """Search documentation for a query."""

# Bad: Kitchen sink tool
@server.tool()
def docs(action: str, query: str, path: str, format: str):
    """Do anything with docs."""
```

### 2. Clear Descriptions
The AI uses your docstrings to decide when to call tools.

```python
@server.tool()
def get_user_by_email(email: str) -> dict:
    """
    Look up a user by their email address.

    Returns user profile including name, role, and last login.
    Returns None if no user found.
    """
```

### 3. Predictable Output
Return structured, consistent data.

```python
# Good: Structured response
return {
    "found": True,
    "results": [...],
    "count": 5
}

# Bad: Variable format
return results if results else "Nothing found"
```

### 4. Graceful Errors
Return error information the AI can understand and act on.

```python
try:
    result = database.query(sql)
    return {"success": True, "data": result}
except DatabaseError as e:
    return {"success": False, "error": str(e), "suggestion": "Check connection"}
```

## Common MCP Patterns

### Read-Only Tools (Safe)
- Search/query tools
- Status checkers
- Metric collectors

### Write Tools (Use Caution)
- File creators
- Database modifiers
- API callers

### Composite Tools
- Multi-step workflows
- Aggregated queries

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- Book Chapter 18: "Tools and the Model Context Protocol"
