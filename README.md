# Inverted-index

## About the project

An inverted index stores the words as index and document names as mapped references. There are many types of inverted indexes but in this project we will implement the word-level inverted index, which stores the position of the word in the document and the document id.

## Built with

This project has been built with Python programming language at Pycharm IDE.

## Getting Started

Once you have cloned the repository there is no configuration you need to do.
All the run files are already configured, but if you have any problem on executing some test or pyhton file you need to write in the program arguments of the file the following sentence.

```
PYTHONUNBUFFERED=1;DATALAKE=C:/Users/Jose Juan/PycharmProjects/Indexer/datalake/;DATAMART=C:/Users/Jose Juan/PycharmProjects/Indexer/datamarts/invertedIndex/
```
## Usage 

In this implementation the builders will create one inverted index using just one document.

The Loader class is the one incharge of loading a document using its id. 
```
loader = DirectoryDocumentLoader()
document = loader.load(37106)
```

You also have the parser classes that the builder needs to create the metadata object.

```
parser = JsonParser()
MetadataBuilder(JsonParser).build(document.metadata)
```

To create the inverted index objet you need to use a tokenizer, the builder requires to build it.

```
invertedIndex = TupleListInvertedIndexBuilder(NltkTokenizer()).build(document)
```

The store class needs a Serializer and a Persister to store the inverted index object.

```
serializer = TupleListInvertedIndexSerializer()
persister = InvertedIndexPersister()
InvertedIndexStore.store(invertedIndex, serializer, persister)
```
## Contact

(c) 2022 José Juan Hernández Gálvez 
<br>Github: https://github.com/josejuanhernandezgalvez<br> 
(c) 2022 David Cruz Sánchez          
Github: https://github.com/Davoestacogido<br>
(c) 2022 Juan Carlos Santana Santana 
<br>Github: https://github.com/JuanCarss<br>
(c) 2022 Jorge Hernández Hernández    
Github: https://github.com/Yorchz
