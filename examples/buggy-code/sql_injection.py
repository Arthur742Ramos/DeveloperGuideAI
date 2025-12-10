"""
SQL Injection Vulnerability Example

This code has SQL injection vulnerabilities. Use AI to find and fix them.
This is a SECURITY exercise - the code intentionally demonstrates bad practices.

Exercise: Identify all injection points and fix them.
"""

import sqlite3


def get_user_by_username(conn, username):
    """
    VULNERABLE: Direct string interpolation in SQL.
    """
    cursor = conn.cursor()
    # Bug: SQL injection via username
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()


def search_products(conn, search_term, category):
    """
    VULNERABLE: Multiple injection points.
    """
    cursor = conn.cursor()
    # Bug: Both search_term and category are injectable
    query = f"""
        SELECT * FROM products
        WHERE name LIKE '%{search_term}%'
        AND category = '{category}'
        ORDER BY name
    """
    cursor.execute(query)
    return cursor.fetchall()


def update_user_email(conn, user_id, new_email):
    """
    VULNERABLE: Even numeric-looking values can be strings.
    """
    cursor = conn.cursor()
    # Bug: user_id might not be validated as numeric
    query = f"UPDATE users SET email = '{new_email}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()


def delete_old_logs(conn, days_old):
    """
    VULNERABLE: Numeric injection.
    """
    cursor = conn.cursor()
    # Bug: days_old could contain SQL
    query = f"DELETE FROM logs WHERE created_at < DATE('now', '-{days_old} days')"
    cursor.execute(query)
    conn.commit()


def get_user_orders(conn, user_id, sort_column="created_at"):
    """
    VULNERABLE: Column name injection.
    """
    cursor = conn.cursor()
    # Bug: sort_column can't use parameterized queries
    # but it still needs validation
    query = f"""
        SELECT * FROM orders
        WHERE user_id = ?
        ORDER BY {sort_column}
    """
    cursor.execute(query, (user_id,))
    return cursor.fetchall()


# Example attacks (for educational purposes)
ATTACK_EXAMPLES = """
Attack 1: Authentication Bypass
  Input: username = "admin' OR '1'='1"
  Query becomes: SELECT * FROM users WHERE username = 'admin' OR '1'='1'
  Result: Returns first user (often admin)

Attack 2: Data Exfiltration
  Input: search_term = "' UNION SELECT username, password, null, null FROM users --"
  Result: Dumps user credentials

Attack 3: Destructive Attack
  Input: user_id = "1; DROP TABLE users; --"
  Result: Deletes entire users table

Attack 4: Time-based Blind Injection
  Input: category = "electronics' AND (SELECT CASE WHEN (1=1) THEN 1 ELSE 1/0 END)='1"
  Result: Can extract data character by character
"""


def demonstrate_vulnerability():
    """Set up a demo database and show the vulnerability."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            email TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO users (username, password, email)
        VALUES ('admin', 'secret123', 'admin@example.com')
    """)
    cursor.execute("""
        INSERT INTO users (username, password, email)
        VALUES ('user1', 'pass456', 'user@example.com')
    """)
    conn.commit()

    print("=== SQL Injection Demonstration ===\n")

    # Normal query
    print("Normal query (username='admin'):")
    result = get_user_by_username(conn, "admin")
    print(f"  Result: {result}\n")

    # Injection attack
    print("Injection attack (username=\"' OR '1'='1\"):")
    result = get_user_by_username(conn, "' OR '1'='1")
    print(f"  Result: {result}")
    print("  (Returned first user without knowing username!)\n")

    print("See ATTACK_EXAMPLES in source for more attack patterns.")

    conn.close()


if __name__ == "__main__":
    demonstrate_vulnerability()
