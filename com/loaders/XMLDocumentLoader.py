from xml.dom import minidom

from com.model.index.InvertedIndexBuilder import InvertedIndexBuilder
from com.model.metadata.MetadataBuilder import MetadataBuilder


class XMLDocumentLoader:
    def load(self, filename):
        file = minidom.parse(filename)
        return InvertedIndexBuilder.build(file.getElementsByTagName('content')), \
               MetadataBuilder(MetadataBuilder().build(file.getElementsByTagName('metadata')))
