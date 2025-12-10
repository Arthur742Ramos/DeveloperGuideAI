"""
API Endpoint Review Target

Review this code for:
- Error handling
- Security issues
- REST conventions
- Code quality

Exercise: Use the code-review prompt template to analyze this file.
"""

from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)


# Issue: Global database connection
db = sqlite3.connect("users.db", check_same_thread=False)


@app.route("/api/users", methods=["GET"])
def get_users():
    # Issue: No pagination
    cursor = db.cursor()
    cursor.execute("SELECT id, username, email FROM users")
    users = cursor.fetchall()
    return jsonify(users)


@app.route("/api/users/<user_id>", methods=["GET"])
def get_user(user_id):
    # Issue: SQL injection possible
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    user = cursor.fetchone()

    # Issue: Returns None without 404
    return jsonify(user)


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json

    # Issue: No input validation
    username = data["username"]
    email = data["email"]
    password = data["password"]

    # Issue: Weak password hashing
    password_hash = hashlib.md5(password.encode()).hexdigest()

    cursor = db.cursor()
    cursor.execute(
        f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password_hash}')"
    )
    db.commit()

    # Issue: Returns password hash in response
    return jsonify({
        "id": cursor.lastrowid,
        "username": username,
        "email": email,
        "password_hash": password_hash
    }), 200  # Issue: Should be 201


@app.route("/api/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    # Issue: No authentication check
    # Issue: No authorization check (can delete any user)

    cursor = db.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    db.commit()

    # Issue: No confirmation of deletion, no 404 if not found
    return "", 200  # Issue: Should be 204


@app.route("/api/search")
def search():
    # Issue: XSS vulnerability - reflects query parameter
    query = request.args.get("q", "")

    cursor = db.cursor()
    # Issue: SQL injection
    cursor.execute(f"SELECT * FROM users WHERE username LIKE '%{query}%'")
    results = cursor.fetchall()

    return jsonify({
        "query": query,  # Issue: Reflects unsanitized input
        "results": results
    })


@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Issue: Timing attack vulnerability
    cursor = db.cursor()
    cursor.execute(
        f"SELECT password FROM users WHERE username = '{username}'"
    )
    result = cursor.fetchone()

    if result:
        password_hash = hashlib.md5(password.encode()).hexdigest()
        # Issue: Direct comparison reveals timing information
        if result[0] == password_hash:
            return jsonify({"status": "ok", "token": "dummy-token"})

    # Issue: Error message reveals whether username exists
    return jsonify({"error": "Invalid username or password"}), 401


# Issue: Debug mode in production code
if __name__ == "__main__":
    app.run(debug=True)
