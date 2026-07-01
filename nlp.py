def analyze_sentiment(text):
    positive_words = ["happy", "good", "great"]
    negative_words = ["sad", "bad", "terrible"]
    score = 0
    for word in text.split():
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    return score
