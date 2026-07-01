import sqlite3
from config import DATABASE_NAME

def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, content TEXT)")
    conn.commit()
    conn.close()

def save_message(msg):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (content) VALUES (?)", msg)
