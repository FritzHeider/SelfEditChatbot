from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        # Perform sentiment analysis
        sentiment_score = self.analyzer.polarity_scores(text)
        # Return sentiment score
        return sentiment_score
