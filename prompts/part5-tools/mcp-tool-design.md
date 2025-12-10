# MCP Tool Design Template

## Purpose

Design effective tools for Model Context Protocol servers. From Chapter 21.

## Tool Definition Template

```json
{
  "name": "tool_name",
  "description": "Clear description of what this tool does and when to use it",
  "inputSchema": {
    "type": "object",
    "properties": {
      "param1": {
        "type": "string",
        "description": "What this parameter is for"
      },
      "param2": {
        "type": "number",
        "description": "What this parameter is for",
        "default": 10
      }
    },
    "required": ["param1"]
  }
}
```

## Description Guidelines

### Good Descriptions

```
"Get current weather conditions for a city using the OpenWeather API.
Returns temperature, conditions, and humidity."

"Search application logs for errors matching a pattern.
Searches the last N hours (default 24). Returns matching log entries."

"Create a new GitHub issue in the specified repository.
Requires title and body. Labels are optional."
```

### Bad Descriptions

```
"Get weather"  # Too vague
"Does stuff with logs"  # Unhelpful
"Issue tool"  # What does it do?
```

## Parameter Naming

### Good Names

```
city_name       # Clear what it is
max_results     # Clear what it limits
include_drafts  # Clear boolean meaning
search_query    # Clear purpose
```

### Bad Names

```
c        # Cryptic
n        # What does this limit?
flag     # Flag for what?
q        # Unclear
```

## Tool Categories

Organize related tools with consistent prefixes:

```
# Ticket tools
ticket_get_context
ticket_search
ticket_update_status

# User tools
user_get_profile
user_get_timeline
user_update_preferences

# Search tools
search_documentation
search_logs
search_similar_tickets
```

## Return Value Design

### Structured Returns (Preferred)

```json
{
  "success": true,
  "data": {
    "temperature": 72,
    "conditions": "sunny",
    "humidity": 45
  }
}
```

### Error Returns

```json
{
  "success": false,
  "error": "City 'asdfgh' not found. Did you mean a real city name?",
  "suggestion": "Check spelling or try a nearby major city"
}
```

## Tool Chaining Design

Design tools that work together:

```
# Investigation flow
get_ticket_context → fetch_user_timeline → analyze_error_logs → search_similar_tickets

# Each tool's output informs the next tool's input
```

## Security Checklist

For each tool:

- [ ] Minimum necessary permissions
- [ ] Input validation (sanitize before using in queries)
- [ ] Output sanitization (no secrets, tokens, PII)
- [ ] Rate limiting consideration
- [ ] Audit logging

## Example: Log Search Tool

```json
{
  "name": "search_logs",
  "description": "Search application logs for entries matching a pattern. Returns up to max_results matching entries from the last N hours. Use for debugging user-reported issues or investigating errors.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "pattern": {
        "type": "string",
        "description": "Search pattern (supports regex)"
      },
      "hours": {
        "type": "number",
        "description": "How many hours back to search",
        "default": 24
      },
      "max_results": {
        "type": "number",
        "description": "Maximum entries to return",
        "default": 100
      },
      "severity": {
        "type": "string",
        "description": "Filter by severity level",
        "enum": ["debug", "info", "warn", "error"]
      }
    },
    "required": ["pattern"]
  }
}
```

## Testing Tools

Before deploying:

1. Test with valid inputs
2. Test with edge cases (empty, very large)
3. Test with invalid inputs
4. Test error handling
5. Test with AI actually calling the tool
