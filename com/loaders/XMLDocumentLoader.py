from xml.dom import minidom

from com.model.index.InvertedIndexBuilder import InvertedIndexBuilder
from com.model.metadata.MetadataBuilder import MetadataBuilder


class XMLDocumentLoader:
    def load(self, filename):
        file = minidom.parse(filename)
        return InvertedIndexBuilder(file.getElementsByTagName('content')), \
               MetadataBuilder(list(file.getElementsByTagName('metadata')))
