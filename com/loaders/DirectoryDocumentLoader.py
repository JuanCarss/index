import os

from com.Document import Document


class DirectoryDocumentLoader:  # FIXME apply $PROJECT_DIR$

    @staticmethod
    def load(fileId):
        result = {"id" : fileId.split("\\")[-1]}
        for filename in os.listdir(fileId):
            with open(fileId + "\\" + filename, "r", encoding="UTF-8") as f:
                result[filename.split(".")[0]] = f.read()
        return Document(**result)
