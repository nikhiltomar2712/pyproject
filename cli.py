def run_cli():
    print("Type your message below. Type exit to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot: Echoing " + user_input)
