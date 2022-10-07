import os
from os.path import abspath, join
from json import dumps

class MetadataPersister:

    @staticmethod
    def persist(metadataToPersist):
        path = abspath(join(__file__ ,"../../../..") + "/invertedIndex/metadata")
        metadataJson = metadataToPersist.to_json(metadataToPersist)
        metadataPath = MetadataPersister._createVariables(path, metadataToPersist)
        MetadataPersister._createDirectory(metadataPath)
        with open(metadataPath + "/" + metadataToPersist.id + ".json", 'w') as f:
            f.write(metadataJson)

    @staticmethod
    def to_json(metadataToPersist):
        return dumps(vars(metadataToPersist))

    @staticmethod
    def _createDirectory(metadataPath):
        if not os.path.isdir(metadataPath): os.makedirs(metadataPath)

    @staticmethod
    def _createVariables(path, metadata):
        metadataPath = path + "/" + metadata.id
        return metadataPath