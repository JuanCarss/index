class MetadataStore:
    @staticmethod
    def store(metadata, serializer, persister):
        persister.persist(serializer.serialize(metadata))
