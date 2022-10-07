class InvertedIndexStore:
    @staticmethod
    def store(invertedIndex, serializer, persister):
        persister.persist(serializer.serialize(invertedIndex))
