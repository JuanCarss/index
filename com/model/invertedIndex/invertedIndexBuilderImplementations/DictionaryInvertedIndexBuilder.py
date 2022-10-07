from collections import defaultdict

from com.model.invertedIndex.InvertedIndex import InvertedIndex
from com.model.tokenizers.NltkTokenizer import NltkTokenizer


class DictionaryInvertedIndexBuilder:

    def __init__(self, reader):
        self.reader = reader

    def build(self, content):
        index = dict()
        self._process_file(content, index)
        return InvertedIndex(index)

    def _process_file(self, file, index):
        for position, word in enumerate(self.reader.tokenize(file[1])):
            if self.reader.check(word): continue
            if word not in index: index[word] = defaultdict(list)
            index[word][file[0]].append(position)


print(DictionaryInvertedIndexBuilder(NltkTokenizer()).build(("001", "probando movidas jaaj")).index)
