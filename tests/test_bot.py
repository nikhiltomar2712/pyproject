import os
from src.chatbot.config import Config
from src.chatbot.bot import ChatBot

def test_chatbot_orchestration():
    # Setup temporary db config
    config = Config()
    config.DATABASE_NAME = "test_chatbot.db"
    
    # Remove existing test DB if any
    if os.path.exists(config.DATABASE_NAME):
        os.remove(config.DATABASE_NAME)
        
    bot = ChatBot(config)
    response = bot.process_message("Hello, how are you?")
    
    assert "Hello" in response
    
    # Verify DB logging
    logs = bot.db.get_recent_logs(limit=2)
    # logs are sorted by ID DESC, so bot response is first, user message is second
    assert len(logs) == 2
    assert logs[0][1] == "Bot"  # sender
    assert logs[1][1] == "User"  # sender
    assert logs[1][2] == "Hello, how are you?"  # message
    
    # Clean up
    if os.path.exists(config.DATABASE_NAME):
        os.remove(config.DATABASE_NAME)
