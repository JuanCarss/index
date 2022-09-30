from com.model.metadata.Metadata import Metadata


class MetadataBuilder:
    def build(self, metadataList):
        return Metadata(**dict(metadataList))

