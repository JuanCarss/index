class InvertedIndex:
    def __init__(self, index):
        self.index = index

    def lookupQuery(self, word):
        return self.index[word]
