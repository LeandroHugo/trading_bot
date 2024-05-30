# src/sentiment_analysis.py
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

if __name__ == "__main__":
    sample_text = "The stock market is expected to rise due to positive earnings reports."
    sentiment = analyze_sentiment(sample_text)
    print(f"Sentiment polarity: {sentiment}")