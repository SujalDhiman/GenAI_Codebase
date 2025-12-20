## Lemmatization

# The output we get after lemmatization is called lemma, which is a root word rather than root stem, the output of stemming. After lemmatization, we will get a valid word that means the same thing.

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

'''
Pos Noun - n
verb - v
adjective - a
adverb -  r
'''

print(lemmatizer.lemmatize('going','n'))

print(lemmatizer.lemmatize('going','a'))

print(lemmatizer.lemmatize('going','v'))


words = ["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]

for word in words:
    print(word+"------>"+lemmatizer.lemmatize(word,'v'))


## Lemmatization takes time  we can use it for text summarization, chatbots

