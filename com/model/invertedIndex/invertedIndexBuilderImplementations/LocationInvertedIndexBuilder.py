from collections import defaultdict

from com.model.invertedIndex.InvertedIndex import InvertedIndex

class LocationInvertedIndexBuilder:

    def __init__(self, reader):
        self.reader = reader

    def build(self, file):
        index = defaultdict()
        self._processfile(index, file)
        return InvertedIndex(index)

    def _processFile(self, index, file):
        (doc_id, content), file_index = file, dict()
        for i, word in enumerate(self.reader.tokenize(content)):
            if self.reader.check(word): continue
            self.indexFile(file_index, i, word)
        self.updateIndex(file_index, index)

    def indexFile(self, file_index, i, word):
        if word not in file_index:
            file_index[word].add_position(i)
        file_index[word].add_position(i)

    def updateIndex(self, file_index, index):
        for word, location in file_index.items():
            index[word].append(location)


class Location:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.positions = []

    def add_position(self, pos):
        self.positions.append(pos)
