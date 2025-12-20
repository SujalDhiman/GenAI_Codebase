corpus = """ Hello Welcome, to Krish Naik's NLP Tutorials.
Please do watch the entire course! to become expert in NLP.
"""

print(corpus)

## Convert Paragraph --> Sentences

from nltk.tokenize import sent_tokenize,word_tokenize, TreebankWordDetokenizer

print(sent_tokenize(corpus))

## Corpus to Words
print(word_tokenize(corpus))

tokenizer = TreebankWordDetokenizer()

print(tokenizer.tokenize(corpus))