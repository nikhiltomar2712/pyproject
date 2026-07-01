def start_bot():
    print("Starting bot...")

def get_greeting():
    return "Hello! How can I help you?"

def handle_user_message(msg):
    if msg == "hello":
        print(get_greeting())
    else:
        print("Unknown command: " + msg)
