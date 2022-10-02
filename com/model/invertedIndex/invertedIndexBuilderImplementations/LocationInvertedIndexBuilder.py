from com.model.invertedIndex.InvertedIndex import InvertedIndex
from com.readers.ContentNltkWordTokenizer import ContentNltkWordTokenizer


class LocationInvertedIndexBuilder:

    def __init__(self, reader):
        self.reader = reader

    def build(self, content):
        index = dict()
        self._process_file(content, index)
        return InvertedIndex(index)

    def _process_file(self, file, index):
        for position, word in enumerate(self.reader.tokenize(file[1])):
            if self.reader.check(word): continue
            if word not in index: index[word] = list()
            self._process_word(index[word], file[0], position)

    def _process_word(self, locationList, fileId, position):
        if not locationList:
            locationList.append(Location(fileId).add_position(position))
            return
        locationList[list(map(Location.doc_id, locationList)).index(fileId)].add_position(position)


class Location:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.positions = []

    def add_position(self, pos):
        self.positions.append(pos)
        return self

    def doc_id(self):
        return self.doc_id


print(LocationInvertedIndexBuilder(ContentNltkWordTokenizer()).build(("001", "probando jaaj movidas jaaj")).index)
