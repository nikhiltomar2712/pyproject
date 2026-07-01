import sqlite3

def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn
