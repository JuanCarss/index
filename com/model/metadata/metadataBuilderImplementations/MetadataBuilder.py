from com.model.metadata.metadataImplementations.Metadata import Metadata


class MetadataBuilder:
    def __init__(self, reader):
        self.reader = reader

    def build(self, metadata):
        return Metadata(**dict(self.reader.tokenize(metadata)))

