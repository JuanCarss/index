class TupleListInvertedIndexSerializer:
    @staticmethod
    def serialize(tupleInvertedIndex):
        result = {}
        for word in tupleInvertedIndex.index:
            result[word] = ('\n'.join('{}\t{}'.format(x[0], x[1]) for x in tupleInvertedIndex[word]))
        return result
