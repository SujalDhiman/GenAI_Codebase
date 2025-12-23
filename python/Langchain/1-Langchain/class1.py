from langchain_community.document_loaders import TextLoader,PyPDFLoader

loader = TextLoader('speech.txt')

document = loader.load()

# print(document)


loader2 = PyPDFLoader('book.pdf')

doc1 = loader2.load()

print(doc1[10],doc1[2],doc1[5])
