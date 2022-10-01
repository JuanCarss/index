from com.model.metadata.metadataImplementations.Metadata import Metadata


class MetadataBuilder:
    def build(self, metadataList):
        return Metadata(**dict(metadataList))

