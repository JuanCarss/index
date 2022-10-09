class InvertedIndex:
    def __init__(self, index):
        self.index = index

    def lookup_query(self, word):
        return self.index[word]
