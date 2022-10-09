from com.loaders.DirectoryDocumentLoader import DirectoryDocumentLoader
from com.model.invertedIndex.InvertedIndexStore import InvertedIndexStore
from com.model.invertedIndex.invertedIndexBuilderImplementations.TupleListInvertedIndexBuilder import TupleListInvertedIndexBuilder
from com.model.invertedIndex.serializers.TupleListInvertedIndexSerializer import TupleListInvertedIndexSerializer
from com.model.metadata.metadataBuilderImplementations.MetadataBuilder import MetadataBuilder
from com.model.persisters.InvertedIndexPersister import InvertedIndexPersister
from com.model.tokenizers.NltkTokenizer import NltkTokenizer
from com.parsers.JsonParser import JsonParser


loader = DirectoryDocumentLoader()
document = loader.load(37106)
parser = JsonParser()
MetadataBuilder(JsonParser).build(document.metadata)
invertedIndex = TupleListInvertedIndexBuilder(NltkTokenizer()).build(document)
serializer = TupleListInvertedIndexSerializer()
persister = InvertedIndexPersister()
InvertedIndexStore.store(invertedIndex, serializer, persister)
