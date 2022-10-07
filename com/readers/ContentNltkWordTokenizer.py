from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


class ContentNltkWordTokenizer:
    def __init__(self):
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stopwords = set(stopwords.words('english'))

    def tokenize(self, content):
        return [word for word in self.tokenizer.tokenize(content)]

    def check(self, word):
        return word in self.stopwords
