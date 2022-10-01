from collections import defaultdict
from com.model.invertedIndex.InvertedIndex import InvertedIndex
from com.readers.ContentNltkWordTokenizer import NltkWordTokenizer


class TupleListInvertedIndexBuilder:
    def __init__(self, reader):
        self.reader = reader

    def build(self, file):
        index = defaultdict(list)
        self._processfile(index, file)
        return InvertedIndex(index)

    def _processfile(self, index, file):
        for i, word in enumerate(self.reader.tokenize(file[1])):
            if self.reader.check(word): continue
            index[word.lower()].append((file[0], i))

    def serialize(self):
        return None  # TODO