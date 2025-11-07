#--------------------------------------------
# Import libraries
#--------------------------------------------
import gensim
from gensim import corpora, models
from gensim.utils import simple_preprocess

#--------------------------------------------
# Step 1: Input Text
#--------------------------------------------
text = ["""I love programming
           Python is my favorite programming language.
           Programming allows me to solve real-world problems."""]

#--------------------------------------------
# Step 2: Tokenization using simple_preprocess()
#--------------------------------------------
tokens = [simple_preprocess(line) for line in text]

#--------------------------------------------
# Step 3: Create Dictionary
#--------------------------------------------
dictionary = corpora.Dictionary(tokens)
print("📘 Dictionary (Word IDs):\n", dictionary.token2id)

#--------------------------------------------
# Step 4: Create Bag of Words (BoW) Representation
#--------------------------------------------
bow_corpus = [dictionary.doc2bow(token) for token in tokens]

print("\n🧩 Bag of Words Representation:")
for doc in bow_corpus:
    print([[dictionary[id], freq] for id, freq in doc])

#--------------------------------------------
# Step 5: Create TF-IDF Model
#--------------------------------------------
tfidf = models.TfidfModel(bow_corpus)

# Apply the model to BoW corpus
tfidf_corpus = tfidf[bow_corpus]

print("\n📊 TF-IDF Representation:")
for doc in tfidf_corpus:
    print([[dictionary[id], round(freq, 3)] for id, freq in doc])