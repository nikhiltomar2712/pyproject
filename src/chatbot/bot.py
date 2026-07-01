from datetime import datetime
from .config import Config
from .memory import ChatMemory
from .nlp import get_intent, analyze_sentiment
from .database import DatabaseManager

class ChatBot:
    """Orchestrator class coordinating memory, NLP, config, and database logs."""

    def __init__(self, config: Config):
        self.config = config
        self.memory = ChatMemory()
        self.db = DatabaseManager(self.config.DATABASE_NAME)

    def process_message(self, message: str) -> str:
        """Route user inputs, update buffers, log turns, and return responses."""
        if not message.strip():
            return "Please say something!"

        # 1. NLP parsing
        intent = get_intent(message)
        sentiment = analyze_sentiment(message)

        # 2. Record turn in memory and Database
        self.memory.add("User", message)
        self.db.log_message("User", message, sentiment)

        # 3. Generate response based on intent routing
        response = self._generate_response(intent, message)

        # 4. Save Bot response
        self.memory.add("Bot", response)
        self.db.log_message("Bot", response, 0)

        return response

    def _generate_response(self, intent: str, message: str) -> str:
        if intent == "greeting":
            return "Hello! I am your AI assistant. How can I help you today?"
        
        if intent == "exit":
            return "Goodbye! Have a wonderful day!"
        
        if intent == "get_weather":
            return "The weather is looking fine and sunny! ☀️"
        
        if intent == "get_time":
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return f"The current system date and time is {now}."
        
        if intent == "help":
            return (
                "Available intents & commands I understand:\n"
                " - Greetings ('hello', 'hi')\n"
                " - Weather queries ('weather')\n"
                " - System time ('time', 'date')\n"
                " - Help instructions ('help')\n"
                " - Termination commands ('exit', 'quit')"
            )
            
        # Fallback response
        return "I'm not quite sure I understand. Could you rephrase that? (Type 'help' to see what I can do)"
