import os

class Config:
    """Application configuration container."""
    API_KEY = os.getenv("CHATBOT_API_KEY", "default-dev-key")
    DATABASE_NAME = os.getenv("CHATBOT_DB", "chatbot_history.db")
    PORT = int(os.getenv("CHATBOT_PORT", 8000))
    DEBUG = os.getenv("CHATBOT_DEBUG", "True").lower() in ("true", "1", "yes")
    LOG_FILE = os.getenv("CHATBOT_LOG_FILE", "bot.log")
