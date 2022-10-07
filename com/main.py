from com.loaders.DirectoryDocumentLoader import DirectoryDocumentLoader
from com.model.invertedIndex.invertedIndexBuilderImplementations.TupleListInvertedIndexBuilder import \
    TupleListInvertedIndexBuilder
from com.model.metadata.metadataBuilderImplementations.MetadataBuilder import MetadataBuilder
from com.model.tokenizers.NltkTokenizer import NltkTokenizer
from com.parsers.JsonParser import JsonParser

loader = DirectoryDocumentLoader()
document = loader.load(r"C:\Users\Jose Juan\PycharmProjects\Indexer\datalake\345")
parser = JsonParser()
MetadataBuilder(JsonParser).build(document.metadata)
TupleListInvertedIndexBuilder(NltkTokenizer()).build((document.id, document.content))
