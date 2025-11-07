###  Assignment No 4 ###

"""Assignment Title : Implement Bi-gram, Tri-gram word sequence and its count in text input
data using NLTK library"""


from nltk import ngrams
from nltk.util import ngrams

#unigram model
n = 1
sentence = 'Earth is the third planet from the Sun in our solar system and the only known celestial body to support life. With a diverse range of ecosystems, it is home to a vast array of plant and animal species, including humans.'

unigrams = ngrams(sentence.split(), n)
print(f"\n***********   UNIGRAM    ************************")
for item in unigrams:
    print(item)
#bigram model
n = 2
sentence = 'Earth is the third planet from the Sun in our solar system and the only known celestial body to support life. With a diverse range of ecosystems, it is home to a vast array of plant and animal species, including humans.'

unigrams = ngrams(sentence.split(), n)
print(f"\n***********   BIGRAM    ************************")
for item in unigrams:
    print(item)

#trigram model
n = 3
sentence = 'Earth is the third planet from the Sun in our solar system and the only known celestial body to support life. With a diverse range of ecosystems, it is home to a vast array of plant and animal species, including humans.'
unigrams = ngrams(sentence.split(), n)
print(f"\n***********   TRIGRAM    ************************")
for item in unigrams:
    print(item)


'''
************    OUTPUT    ********************

***********   UNIGRAM    ************************
('Earth',)
('is',)
('the',)
('third',)
('planet',)
('from',)
('the',)
('Sun',)
('in',)
('our',)
('solar',)
('system',)
('and',)
('the',)
('only',)
('known',)
('celestial',)
('body',)
('to',)
('support',)
('life.',)
('With',)
('a',)
('diverse',)
('range',)
('of',)
('ecosystems,',)
('it',)
('is',)
('home',)
('to',)
('a',)
('vast',)
('array',)
('of',)
('plant',)
('and',)
('animal',)
('species,',)
('including',)
('humans.',)

***********   BIGRAM    ************************
('Earth', 'is')
('is', 'the')
('the', 'third')
('third', 'planet')
('planet', 'from')
('from', 'the')
('the', 'Sun')
('Sun', 'in')
('in', 'our')
('our', 'solar')
('solar', 'system')
('system', 'and')
('and', 'the')
('the', 'only')
('only', 'known')
('known', 'celestial')
('celestial', 'body')
('body', 'to')
('to', 'support')
('support', 'life.')
('life.', 'With')
('With', 'a')
('a', 'diverse')
('diverse', 'range')
('range', 'of')
('of', 'ecosystems,')
('ecosystems,', 'it')
('it', 'is')
('is', 'home')
('home', 'to')
('to', 'a')
('a', 'vast')
('vast', 'array')
('array', 'of')
('of', 'plant')
('plant', 'and')
('and', 'animal')
('animal', 'species,')
('species,', 'including')
('including', 'humans.')

***********   TRIGRAM    ************************
('Earth', 'is', 'the')
('is', 'the', 'third')
('the', 'third', 'planet')
('third', 'planet', 'from')
('planet', 'from', 'the')
('from', 'the', 'Sun')
('the', 'Sun', 'in')
('Sun', 'in', 'our')
('in', 'our', 'solar')
('our', 'solar', 'system')
('solar', 'system', 'and')
('system', 'and', 'the')
('and', 'the', 'only')
('the', 'only', 'known')
('only', 'known', 'celestial')
('known', 'celestial', 'body')
('celestial', 'body', 'to')
('body', 'to', 'support')
('to', 'support', 'life.')
('support', 'life.', 'With')
('life.', 'With', 'a')
('With', 'a', 'diverse')
('a', 'diverse', 'range')
('diverse', 'range', 'of')
('range', 'of', 'ecosystems,')
('of', 'ecosystems,', 'it')
('ecosystems,', 'it', 'is')
('it', 'is', 'home')
('is', 'home', 'to')
('home', 'to', 'a')
('to', 'a', 'vast')
('a', 'vast', 'array')
('vast', 'array', 'of')
('array', 'of', 'plant')
('of', 'plant', 'and')
('plant', 'and', 'animal')
('and', 'animal', 'species,')
('animal', 'species,', 'including')
('species,', 'including', 'humans.')

'''
'''Explanation:

Introduction:

N-grams are sequences of n consecutive words in a text.

Common types:

Unigram: Single words (n=1)

Bigram: Two consecutive words (n=2)

Trigram: Three consecutive words (n=3)

N-grams are widely used in text analytics, predictive text, NLP models, and language modeling.

Importing Libraries:

nltk library is used for NLP tasks.

ngrams from nltk.util generates n-grams from a sequence of words.

Unigram Model:

n = 1 generates single words from the sentence.

Each word is treated as an individual token.

Example output: ('Earth',), ('is',), ('the',), ...

Bigram Model:

n = 2 generates pairs of consecutive words.

Useful for analyzing word combinations and context.

Example output: ('Earth', 'is'), ('is', 'the'), ('the', 'third'), ...

Trigram Model:

n = 3 generates sequences of three consecutive words.

Captures slightly longer context compared to bigrams.

Example output: ('Earth', 'is', 'the'), ('is', 'the', 'third'), ...

Output Interpretation:

Shows all possible word sequences in the sentence.

Unigrams are single words, bigrams are word pairs, trigrams are word triplets.

These sequences are useful for predictive typing, text generation, and NLP analysis.

Real-Time Applications:

Search engines: Improve query suggestions and autocomplete.

Chatbots / AI systems: Understand word context and generate meaningful responses.

Text Mining / Analytics: Analyze frequent word patterns in documents or social media.

Steps to Run from Scratch:

# Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

# Install NLTK library
python -m pip install nltk

# Optional: Download NLTK resources if needed
python -m nltk.downloader punkt'''