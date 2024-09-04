import unittest
from textblob import TextBlob
from sentiment import analyze_sentiment


class TestSentimentAnalysis(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(analyze_sentiment("I love this product!"), "Positive")

    def test_negative(self):
        self.assertEqual(analyze_sentiment("This is the worst experience ever."), "Negative")

    def test_neutral(self):
        self.assertEqual(analyze_sentiment("It’s okay, not great but not bad."), "Neutral")

    def test_mixed(self):
        self.assertEqual(analyze_sentiment("I love the service but the product is bad."), "Mixed")


if __name__ == "__main__":
    unittest.main()
