## Stemming - reducing word to its word stem

words = ["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]

## First Stemming Technique

#1 Porter Stemming

from nltk.stem import PorterStemmer

stemming = PorterStemmer()

for word in words:
    print(word+"------>"+stemming.stem(word))

## disadvantage of stemming is sometimes u might not get the exact word stem e.g History which in turn changes the meaning of word another e.g congratulations


#2) Regexp Stemmer Class

from nltk.stem import RegexpStemmer

reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)

print(reg_stemmer.stem('eating'))

print(reg_stemmer.stem('ingeating'))


#3) Snowball Stemmer -- better

from nltk.stem import SnowballStemmer

snow_stemmer = SnowballStemmer('english')

for word in words:
    print(word+"----->"+snow_stemmer.stem(word))


## difference

print(stemming.stem("fairly"),stemming.stem("sportingly"))


print(snow_stemmer.stem("fairly"),snow_stemmer.stem("sportingly"))
