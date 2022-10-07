from com.loaders.DirectoryDocumentLoader import DirectoryDocumentLoader
from com.model.invertedIndex.InvertedIndexStore import InvertedIndexStore
from com.model.invertedIndex.invertedIndexBuilderImplementations.TupleListInvertedIndexBuilder import \
    TupleListInvertedIndexBuilder
from com.model.invertedIndex.serializers.TupleListInvertedIndexSerializer import TupleListInvertedIndexSerializer
from com.model.persisters.InvertedIndexPersister import InvertedIndexPersister
from com.readers.ContentNltkWordTokenizer import ContentNltkWordTokenizer

loader = DirectoryDocumentLoader()
document = loader.load(r"C:\Users\david\OneDrive\Documentos\GitHub\python_BigData\index\datalake\Dracula.xml")
reader = ContentNltkWordTokenizer()
index = TupleListInvertedIndexBuilder(reader).build((document.id, document.content))
serializer = TupleListInvertedIndexSerializer()
persister = InvertedIndexPersister()
InvertedIndexStore().store(index, serializer, persister)
