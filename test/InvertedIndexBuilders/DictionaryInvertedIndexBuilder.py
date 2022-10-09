from collections import defaultdict

from com.model.invertedIndex.InvertedIndex import InvertedIndex
from com.model.tokenizers.NltkTokenizer import NltkTokenizer


class DictionaryInvertedIndexBuilder:

    def __init__(self, reader):
        self.reader = reader

    def build(self, document):
        index = dict()
        self._process_file(document, index)
        return InvertedIndex(index)

    def _process_file(self, document, index):
        for position, word in enumerate(self.reader.tokenize(document.content)):
            if self.reader.check(word): continue
            if word not in index: index[word] = defaultdict(list)
            index[word][document.id].append(position)
