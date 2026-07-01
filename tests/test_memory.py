from src.chatbot.memory import ChatMemory

def test_chat_memory_addition():
    memory = ChatMemory(max_history=3)
    memory.add("User", "Hello")
    memory.add("Bot", "Hi")
    
    assert len(memory.history) == 2
    assert memory.history[0]["role"] == "User"
    assert memory.history[1]["role"] == "Bot"

def test_chat_memory_sliding_window():
    memory = ChatMemory(max_history=2)
    memory.add("User", "Msg 1")
    memory.add("Bot", "Msg 2")
    memory.add("User", "Msg 3")
    
    assert len(memory.history) == 2
    assert memory.history[0]["text"] == "Msg 2"
    assert memory.history[1]["text"] == "Msg 3"

def test_chat_memory_clear():
    memory = ChatMemory()
    memory.add("User", "Test")
    memory.clear()
    assert len(memory.history) == 0

def test_get_last_messages():
    memory = ChatMemory()
    memory.add("User", "Msg 1")
    memory.add("Bot", "Msg 2")
    
    last = memory.get_last_messages(1)
    assert len(last) == 1
    assert last[0]["text"] == "Msg 2"
    
    assert len(memory.get_last_messages(0)) == 0
