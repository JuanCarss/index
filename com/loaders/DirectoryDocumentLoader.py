from xml.etree import ElementTree

from com.Document import Document


class DirectoryDocumentLoader:
    def load(self, filename):
        with open(filename, encoding="UTF-8") as f: file = ElementTree.parse(f).getroot()
        return Document(file[0].text, file[1].text, filename.split("\\")[-1].split(".")[0])  # FIXME
