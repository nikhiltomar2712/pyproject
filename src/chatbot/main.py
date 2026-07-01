import sys
from .config import Config
from .bot import ChatBot

def main():
    """Main CLI entry point."""
    config = Config()
    bot = ChatBot(config)

    print("==============================================")
    print("      Welcome to AI ChatBot (pyproject)       ")
    print("==============================================")
    print("Type your message and press Enter. (Type 'exit' to quit)")
    print("----------------------------------------------")

    try:
        while True:
            user_input = input("\nYou: ")
            if not user_input.strip():
                continue
                
            response = bot.process_message(user_input)
            print(f"Bot: {response}")

            if get_intent_for_exit(user_input):
                break
    except (KeyboardInterrupt, EOFError):
        print("\nBot: Session interrupted. Goodbye!")
        sys.exit(0)

def get_intent_for_exit(text: str) -> bool:
    """Helper to detect if user wants to exit from input directly."""
    words = text.lower().strip().split()
    return any(w in words for w in ["exit", "quit", "bye", "goodbye"])

if __name__ == "__main__":
    main()
