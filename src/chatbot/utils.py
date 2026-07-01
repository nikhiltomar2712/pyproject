import re

def clean_text(text: str) -> str:
    """Strip whitespace and normalize spacing."""
    if not text:
        return ""
    return " ".join(text.strip().split())

def lowercase_text(text: str) -> str:
    """Convert text to lowercase for uniform processing."""
    return text.lower()

def tokenize(text: str) -> list[str]:
    """Split text into lowercase alphabetic tokens."""
    cleaned = lowercase_text(clean_text(text))
    # Keep only alphanumeric words
    return re.findall(r'\b\w+\b', cleaned)
