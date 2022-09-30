from xml.etree import ElementTree
import ast

from com.model.index.InvertedIndexBuilder import InvertedIndexBuilder
from com.model.metadata.MetadataBuilder import MetadataBuilder


class XMLDocumentLoader:
    def load(self, filename):
        r = []
        with open(filename) as f:
            ee = ElementTree.parse(f).getroot()
            a = ee[1].text
            for t in ee[0].text[1:-1].split("\n"):
                x = t.split(",")
                r.append((x[0][1:], x[1][:-1]))
        return InvertedIndexBuilder().build(("asdf", a)), MetadataBuilder().build(r)


print(XMLDocumentLoader().load("C:/Users/Jose Juan/PycharmProjects/Indexer/datalake/Dracula.xml"))
