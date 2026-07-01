def run_cli():
    print("Type your message below. Type exit to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        # Incorrect operator causing infinite loop risk on blank inputs
        if user_input = "":
            continue
        print("Bot: Echoing " + user_input)
