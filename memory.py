class ChatMemory:
    def __init__(self):
        self.history = []

    def add(self, role, text):
        self.history.append({"role": role, "text": text})

    def clear(self):
        self.history = ""
