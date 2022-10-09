from com.model.invertedIndex.InvertedIndex import InvertedIndex


class LocationInvertedIndexBuilder:

    def __init__(self, reader):
        self.reader = reader

    def build(self, document):
        index = dict()
        self._process_document(document, index)
        return InvertedIndex(index)

    def _process_document(self, document, index):
        for position, word in enumerate(self.reader.tokenize(document.content)):
            if self.reader.check(word): continue
            if word not in index: index[word] = list()
            self._process_word(index[word], document.id, position)

    def _process_word(self, locationList, documentId, position):
        if not locationList:
            locationList.append(Location(documentId).add_position(position))
            return
        locationList[list(map(Location.doc_id, locationList)).index(documentId)].add_position(position)


class Location:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.positions = []

    def add_position(self, pos):
        self.positions.append(pos)
        return self

    def doc_id(self):
        return self.doc_id


