from collections import defaultdict
from com.model.invertedIndex.InvertedIndex import InvertedIndex


class TupleListInvertedIndexBuilder:
    def __init__(self, reader):
        self.reader = reader

    def build(self, document):
        index = defaultdict(list)
        self._process_document(index, document)
        return InvertedIndex(index)

    def _process_document(self, index, document):
        for i, word in enumerate(self.reader.tokenize(document.content)):
            if self.reader.check(word): continue
            index[word.lower()].append((document.id, i))
