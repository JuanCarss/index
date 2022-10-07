from collections import defaultdict
from com.model.invertedIndex.InvertedIndex import InvertedIndex


class TupleListInvertedIndexBuilder:
    def __init__(self, reader):
        self.reader = reader

    def build(self, file):
        index = defaultdict(list)
        self._process_file(index, file)
        return InvertedIndex(index)

    def _process_file(self, index, file):
        for i, word in enumerate(self.reader.tokenize(file[1])):
            if self.reader.check(word): continue
            index[word.lower()].append((file[0], i))
