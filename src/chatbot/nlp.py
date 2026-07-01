from .utils import clean_text, tokenize

def analyze_sentiment(text: str) -> int:
    """Calculate crude sentiment score (-1 to 1) based on keyword matching."""
    positive_words = {"happy", "good", "great", "excellent", "wonderful", "cool", "fine"}
    negative_words = {"sad", "bad", "terrible", "horrible", "awful", "angry", "poor"}
    
    tokens = tokenize(text)
    score = 0
    for token in tokens:
        if token in positive_words:
            score += 1
        elif token in negative_words:
            score -= 1
            
    # Normalize score
    if score > 0:
        return 1
    elif score < 0:
        return -1
    return 0

def get_intent(text: str) -> str:
    """Classify user intent based on keyword/pattern matching."""
    tokens = set(tokenize(text))
    
    if any(greet in tokens for greet in ["hello", "hi", "hey", "greetings"]):
        return "greeting"
    if any(exit_word in tokens for exit_word in ["exit", "quit", "bye", "goodbye"]):
        return "exit"
    if "weather" in tokens:
        return "get_weather"
    if "time" in tokens or "date" in tokens:
        return "get_time"
    if any(help_word in tokens for help_word in ["help", "info", "commands"]):
        return "help"
        
    return "unknown"
