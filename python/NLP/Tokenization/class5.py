## Bag of Words Implementation

corpus="""
I love machine learning and data science.
Machine learning is fun and powerful.
Data science uses machine learning techniques.
I enjoy learning new programming concepts.
Programming in python is fun.
Python is widely used in data science,
Machine learning models learn from data.
Data analysis is important in data science.
I love programming and problem solving.
Learning machine learning improves problem solving.
"""
import re

from nltk.corpus import stopwords

from nltk.tokenize import sent_tokenize

from nltk.stem import PorterStemmer

ps = PorterStemmer()

sentences = sent_tokenize(corpus)

new_sentences = []

for sentence in sentences:
    review = re.sub('[^a-zA-Z]',' ',sentence)
    review = review.lower().split()
    review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    new_sentences.append(review)



# create bag of woods

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=2500) # pick top 2500 words

X = cv.fit_transform(new_sentences).toarray()

print(X) # created a bag of words not binary

    



