from com.model.metadata.metadataImplementations.Metadata import Metadata


class MetadataBuilder:
    def __init__(self, parser):
        self.parser = parser

    def build(self, metadata):
        return Metadata(**dict(self.parser.parse(metadata)))

