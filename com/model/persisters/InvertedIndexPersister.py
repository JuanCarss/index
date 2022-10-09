import os
from os.path import abspath, join
import shutil


class InvertedIndexPersister:

    @staticmethod
    def persist(invertedIndexToPersist):
        if os.path.exists(os.environ["DATAMART"]): shutil.rmtree(os.environ["DATAMART"])
        for word in invertedIndexToPersist:
            wordPath = InvertedIndexPersister._createVariables(word, os.environ["DATAMART"])
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
