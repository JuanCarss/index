import os
from os.path import realpath, dirname, abspath, join

class InvertedIndexPersister:

    @staticmethod
    def persist(invertedIndexToPersist):
        path = abspath(join(__file__ ,"../../../..") + "/invertedIndex/indexs")
        for word in invertedIndexToPersist:
            wordPath = InvertedIndexPersister._createVariables(word, path)
            InvertedIndexPersister._createDirectory(wordPath)
            with open(wordPath + "/" + word + ".tsv", 'w') as f:
                f.write("id\tposition\n" + invertedIndexToPersist[word])

    @staticmethod
    def _createDirectory(wordPath):
        if not os.path.isdir(wordPath): os.makedirs(wordPath)

    @staticmethod
    def _createVariables(word, path):
        wordPath = path + "/" + word[0] + "/" + word[0:2]
        return wordPath


InvertedIndexPersister.persist({'wasd': '\nasdf\tasdf\nasdf\tasdf', 'bas': '\nasdf\tasdf'})
