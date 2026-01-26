import sqlite3
import hashlib

DB_NAME = "users.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hash_password(password))
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def login_user(username, password):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM users WHERE username = ? AND password = ?",
        (username, hash_password(password))
    )

    result = cursor.fetchone()
    conn.close()

    return result is not None


def delete_user(username, password):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE username = ? AND password = ?",
        (username, hash_password(password))
    )

    deleted = cursor.rowcount
    conn.commit()
    conn.close()

    return deleted > 0
