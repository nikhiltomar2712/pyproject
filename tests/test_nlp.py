from src.chatbot.nlp import analyze_sentiment, get_intent

def test_analyze_sentiment():
    assert analyze_sentiment("I am extremely happy and feeling good!") == 1
    assert analyze_sentiment("This is so sad and terrible.") == -1
    assert analyze_sentiment("Hello bot, what is the time?") == 0

def test_get_intent():
    assert get_intent("Hello, how are you?") == "greeting"
    assert get_intent("What is the weather today?") == "get_weather"
    assert get_intent("Can you tell me the current time?") == "get_time"
    assert get_intent("Goodbye for now.") == "exit"
    assert get_intent("Please help me with commands.") == "help"
    assert get_intent("some random phrase") == "unknown"
