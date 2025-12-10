# Solution: SQL Injection Vulnerabilities

## Fix 1: Use Parameterized Queries

```python
# Buggy
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)

# Fixed
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

## Fix 2: Multiple Parameters

```python
# Buggy
query = f"""
    SELECT * FROM products
    WHERE name LIKE '%{search_term}%'
    AND category = '{category}'
"""

# Fixed
query = """
    SELECT * FROM products
    WHERE name LIKE ?
    AND category = ?
"""
cursor.execute(query, (f"%{search_term}%", category))
```

## Fix 3: Whitelist Column Names

```python
# Buggy
query = f"SELECT * FROM orders ORDER BY {sort_column}"

# Fixed
ALLOWED_COLUMNS = {"created_at", "total", "status", "id"}

def get_user_orders(conn, user_id, sort_column="created_at"):
    if sort_column not in ALLOWED_COLUMNS:
        sort_column = "created_at"  # Default to safe value

    query = f"""
        SELECT * FROM orders
        WHERE user_id = ?
        ORDER BY {sort_column}
    """
    cursor.execute(query, (user_id,))
```

## Fix 4: Type Validation

```python
# Buggy
query = f"DELETE FROM logs WHERE created_at < DATE('now', '-{days_old} days')"

# Fixed
def delete_old_logs(conn, days_old):
    # Validate input type
    days_old = int(days_old)  # Raises ValueError if not numeric
    if days_old < 0 or days_old > 365:
        raise ValueError("days_old must be between 0 and 365")

    query = "DELETE FROM logs WHERE created_at < DATE('now', ? || ' days')"
    cursor.execute(query, (f"-{days_old}",))
```

## Complete Fixed Version

```python
def get_user_by_username(conn, username):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )
    return cursor.fetchone()


def search_products(conn, search_term, category):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM products
        WHERE name LIKE ?
        AND category = ?
        ORDER BY name
        """,
        (f"%{search_term}%", category)
    )
    return cursor.fetchall()


def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    # Validate user_id is numeric
    user_id = int(user_id)
    cursor.execute(
        "UPDATE users SET email = ? WHERE id = ?",
        (new_email, user_id)
    )
    conn.commit()
```

## Key Principles

1. **Never concatenate user input into SQL**
2. **Always use parameterized queries** (?, :name, %s depending on driver)
3. **Whitelist for dynamic identifiers** (column names, table names)
4. **Validate types** even with parameterized queries
5. **Use ORM when possible** (SQLAlchemy, Django ORM, etc.)

## AI Security Review Tips

Ask AI to:
1. "Review this code for SQL injection vulnerabilities"
2. "Show me attack payloads that would exploit this code"
3. "Rewrite using parameterized queries"
4. "Identify all places where user input reaches SQL"
