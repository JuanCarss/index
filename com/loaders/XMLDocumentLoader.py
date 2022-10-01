from xml.etree import ElementTree

from com.Document import Document


class XMLDocumentLoader:
    def load(self, filename):
        with open(filename) as f: file = ElementTree.parse(f).getroot()
        return Document(file[0].text, file[1].text)
