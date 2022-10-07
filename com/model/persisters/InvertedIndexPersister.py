import os


class InvertedIndexPersister:

    @staticmethod
    def persist(invertedIndexToPersist, path=r"/Users/JJ/PycharmProjects/InvertedIndex/InvertedIndex"):
        for word in invertedIndexToPersist:
            wordPath, filePath = InvertedIndexPersister._createVariables(word, path)
            InvertedIndexPersister._createDirectory(wordPath)
            with open(wordPath + "/" + word + ".tsv", 'w') as f:
                f.write("id\tposition" + invertedIndexToPersist[word])

    @staticmethod
    def _createDirectory(wordPath):
        if not os.path.isdir(wordPath): os.makedirs(wordPath)

    @staticmethod
    def _createVariables(word, path):
        wordPath = path + "/" + word[0] + "/" + word[0:2]
        filepath = wordPath + "/" + word + ".tsv"
        return wordPath, filepath


InvertedIndexPersister.persist({'wasd': '\nasdf\tasdf\nasdf\tasdf', 'bas': '\nasdf\tasdf'})
