class InvertedIndexStore:
    @staticmethod
    def store(invertedIndex, serializer, persister):
        persister.persiste(serializer.serialize(invertedIndex))
