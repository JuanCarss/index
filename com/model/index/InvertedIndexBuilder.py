from collections import defaultdict

from com.model.index.invertedIndexImplementations.InvertedIndex import InvertedIndex
from com.readers.NltkWordTokenizer import NltkWordTokenizer


class InvertedIndexBuilder:
    def build(self, *files):
        index = defaultdict(list)
        for file in files: self._processfile(index, file)
        return InvertedIndex(index)

    def _processfile(self, index, file):
        for i, word in enumerate(NltkWordTokenizer.tokenize(file[1])):
            index[word].append((file[0], i))
