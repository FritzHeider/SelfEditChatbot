import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class Preprocessor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def preprocess(self, text):
        # Tokenization
        tokens = word_tokenize(text.lower())
        # Removing stop words and stemming
        tokens = [self.stemmer.stem(token) for token in tokens if token not in self.stop_words]
        return tokens
