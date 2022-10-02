from collections import defaultdict

from com.model.invertedIndex.InvertedIndex import InvertedIndex
from com.readers.ContentNltkWordTokenizer import ContentNltkWordTokenizer


class LocationInvertedIndexBuilder:

    def __init__(self, reader):
        self.reader = reader

    def build(self, content):
        index = dict()
        self._processfile(content, index)
        return InvertedIndex(index)

    def _processfile(self, file, index):
        for position, word in enumerate(self.reader.tokenize(file[1])):
            if self.reader.check(word): continue
            if word not in index: index[word] = defaultdict(Location(file[0]))
            index[word].add_position(position)


class Location:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.positions = []

    def add_position(self, pos):
        self.positions.append(pos)


print(LocationInvertedIndexBuilder(ContentNltkWordTokenizer()).build(("001", "probando movidas jaaj")).index)
