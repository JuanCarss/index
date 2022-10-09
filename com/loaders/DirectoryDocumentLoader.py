import os
from os.path import abspath, join

from com.Document import Document


class DirectoryDocumentLoader:

    @staticmethod
    def load(fileId):
        fileId = os.environ["DATALAKE"] + str(fileId)  # TODO
        result = {"id": fileId.split("\\")[-1]}
        for filename in os.listdir(fileId):
            with open(fileId + "\\" + filename, "r", encoding="UTF-8") as f:
                result[filename.split(".")[0]] = f.read()
        return Document(**result)
