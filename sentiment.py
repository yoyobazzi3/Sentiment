from textblob import TextBlob


def analyze_sentiment(text):
    """
    This function takes a string input, analyzes the sentiment,
    and returns 'Positive', 'Negative', or 'Neutral' based on the sentiment polarity.
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"


# Test the function manually
if __name__ == "__main__":
    sample_texts = [
        "I absolutely love this product!",  # Positive sentiment
        "This is the worst experience ever.",  # Negative sentiment
        "It’s okay, not great but not bad.",  # Neutral sentiment
    ]

    for text in sample_texts:
        sentiment = analyze_sentiment(text)
        print(f"Text: {text}\nSentiment: {sentiment}\n")
