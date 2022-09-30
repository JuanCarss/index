from collections import defaultdict
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))


class InvertedIndexConstructor:
    def build(self, files):
        index = defaultdict(list)
        for file in files: self._processFile(index, file)
        self._removeInvalidKeys(index)
        return InvertedIndex(index)

    def append(self, index, *files):
        for file in files: self._updateIndex(index, file)

    def remove(self, invertedIndex, fileToRemove):
        for word in invertedIndex.index:
            invertedIndex.index[word] = list(filter(lambda t: fileToRemove not in t, invertedIndex.index[word]))
        self._removeInvalidKeys(invertedIndex.index)

    def _removeInvalidKeys(self, index):
        for k, v in list(index.items()):
            if len(v) == 0: del index[k]

    def _processFile(self, index, file):
        tokenizer = RegexpTokenizer(r'\w+')
        for i, word in (enumerate(tokenizer.tokenize(file[1]))):
            if word in stop_words: continue
            index[word].append((file[0], i))

    def _updateIndex(self, invertedIndex, file):
        self.remove(invertedIndex, file[0])
        self._processFile(invertedIndex.index, file)


class InvertedIndex:
    def __init__(self, index):
        self.index = index

    def resultsFor(self, word):
        return self.index[word]
