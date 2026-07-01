import sqlite3
from typing import Generator
from contextlib import contextmanager

class DatabaseManager:
    """Manages SQLite context and connection life cycle."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.init_db()

    @contextmanager
    def connection(self) -> Generator[sqlite3.Connection, None, None]:
        """Provide a transactional scope around a series of queries."""
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def init_db(self) -> None:
        """Initialize database schema."""
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS chat_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    sender TEXT NOT NULL,
                    message TEXT NOT NULL,
                    sentiment INTEGER
                )
                """
            )

    def log_message(self, sender: str, message: str, sentiment: int) -> None:
        """Save a message turn into the database log."""
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO chat_logs (sender, message, sentiment) VALUES (?, ?, ?)",
                (sender, message, sentiment)
            )

    def get_recent_logs(self, limit: int = 50) -> list[tuple]:
        """Fetch historical records."""
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT timestamp, sender, message, sentiment FROM chat_logs ORDER BY id DESC LIMIT ?",
                (limit,)
            )
            return cursor.fetchall()
