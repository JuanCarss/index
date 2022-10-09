import os
import time
import unittest
from os import listdir
from os.path import join, abspath
from com.loaders.DirectoryDocumentLoader import DirectoryDocumentLoader
from com.model.invertedIndex.invertedIndexBuilderImplementations.TupleListInvertedIndexBuilder import \
    TupleListInvertedIndexBuilder
from com.model.tokenizers.NltkTokenizer import NltkTokenizer
from invertedIndexBuilders.LocationInvertedIndexBuilder import LocationInvertedIndexBuilder

from invertedIndexBuilders.DictionaryInvertedIndexBuilder import DictionaryInvertedIndexBuilder


class InvertedIndexTimeTest(unittest.TestCase):

    def getAllDocuments(self):
        loader = DirectoryDocumentLoader()
        dir_paths = [f for f in listdir(os.environ["DATALAKE"])]
        documents = [loader.load(path) for path in dir_paths]
        return documents

    def setup_method(self):
        self.documents = self.getAllDocuments()
        self.reader = NltkTokenizer()
        self.dic_version = DictionaryInvertedIndexBuilder(self.reader)
        self.object_version = LocationInvertedIndexBuilder(self.reader)
        self.tuple_version = TupleListInvertedIndexBuilder(self.reader)

    def test_build_time_dic(self):
        self.setup_method()
        start_time = time.time()
        for _ in range(0, 10):
            for document in self.documents:
                self.dic_version.build(document)
        print("execution mean time for document to build dicts of dicts: ", (time.time() - start_time) / 90)

    def test_build_time_tuple(self):
        self.setup_method()
        start_time = time.time()
        for _ in range(0, 10):
            for document in self.documents:
                self.tuple_version.build(document)
        print("execution mean time for document to build dicts of tuples: ", (time.time() - start_time) / 90)

    def test_build_time_object(self):
        self.setup_method()
        start_time = time.time()
        for _ in range(0, 10):
            for document in self.documents:
                self.object_version.build(document)
        print("execution mean time for document to build dicts of objects: ", (time.time() - start_time) / 90)
