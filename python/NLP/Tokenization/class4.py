## Parts of Speech Tagging

# categorize words into different parts of speech

paragraph = """I have three visions for India. In 3000 years of our history people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards the Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture and their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others. That is why my FIRST VISION is that of FREEDOM. I believe that India got its first vision of this in 1857, when we started the war of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us.
"""

from nltk.tokenize import sent_tokenize, word_tokenize

import nltk

from nltk.corpus import stopwords

sentences = sent_tokenize(paragraph)

for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    words = [word for word in words if word not in set(stopwords.words("english"))]
    pos_tag = nltk.pos_tag(words) # parts of speech tagging
    print(pos_tag)



print(nltk.pos_tag("Chittor Fort is a Magnificent Fort".split()))



