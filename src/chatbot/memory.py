class ChatMemory:
    """Manages conversational memory buffer with sliding window capabilities."""
    
    def __init__(self, max_history: int = 20):
        self.history: list[dict[str, str]] = []
        self.max_history = max_history

    def add(self, role: str, text: str) -> None:
        """Add a conversation turn to the memory history."""
        self.history.append({"role": role, "text": text})
        # Keep sliding window size bounded
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def clear(self) -> None:
        """Clear memory buffer."""
        self.history = []

    def get_last_messages(self, count: int) -> list[dict[str, str]]:
        """Retrieve last N messages from history."""
        if count <= 0:
            return []
        return self.history[-count:]
