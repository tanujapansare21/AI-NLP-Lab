##Assignment No.02##

#Title:Assignment to implement Bag of Words and TFIDF using Gensim library.
import gensim
from gensim import corpora
from gensim.utils import simple_preprocess

text2 = ["""I love programming
         Python is my favorite programming language.
         Programming allows me to solve real-world problems."""]

tokens2 = [[item for item in line.split()] for line in text2]
g_dict2 = corpora.Dictionary(tokens2)

print("The dictionary has: " + str(len(g_dict2)) + " tokens\n")
print(g_dict2.token2id)

g_bow2 = [g_dict2.doc2bow(token, allow_update=True) for token in tokens2]
print("Bag of Words : ", g_bow2)

text3 = ["""I love programming
         Python is my favorite programming language.
         Programming allows me to solve real-world problems."""]

g_dict3 = corpora.Dictionary([simple_preprocess(line) for line in text3])
g_bow3 = [g_dict3.doc2bow(simple_preprocess(line)) for line in text3]

print("\nDictionary : ")
for item in g_bow3:
    print([[g_dict3[id], freq] for id, freq in item])


    
##OUTPUT##
'''
The dictionary has: 12 tokens

{'I': 0, 'Python': 1, 'allows': 2, 'favorite': 3, 'is': 4, 'language.': 5, 'love': 6, 'me': 7, 'my': 8, 'programming': 9, 'real-world': 10, 'solve': 11}
Bag of Words :  [[(0, 1), (6, 1), (9, 1)], [(1, 1), (3, 1), (4, 1), (5, 1), (8, 1), (9, 1)], [(2, 1), (7, 1), (10, 1), (11, 1), (9, 1)]]

Dictionary : 
[['I', 1], ['love', 1], ['programming', 1]]
[['Python', 1], ['favorite', 1], ['is', 1], ['language', 1], ['my', 1], ['programming', 1]]
[['allows', 1], ['me', 1], ['real-world', 1], ['solve', 1], ['programming', 1]]

'''
#steps to run
# python -m pip install gensim
# python gensim_word2vec.py

'''Explanation:

Introduction:

Bag of Words (BoW) and TF-IDF are common techniques in Natural Language Processing (NLP) used to represent text as numerical vectors.

BoW: Converts text into a vector based on the frequency of each word, ignoring grammar and word order.

TF-IDF: (Term Frequency-Inverse Document Frequency) gives importance to words that are unique in a document and reduces the weight of common words.

Tokenization:

Sentences are split into individual words (tokens) using split() or simple_preprocess().

This helps the model analyze each word separately.

Dictionary Creation:

corpora.Dictionary() maps each unique token to a unique ID.

Example: 'I': 0, 'Python': 1, 'programming': 9

Bag of Words (BoW) Representation:

doc2bow() converts each sentence into a list of tuples (word_id, frequency).

This represents how many times each word appears in the text.

Example: [(0, 1), (6, 1), (9, 1)] → Words with IDs 0, 6, 9 appear once each.

Output Interpretation:

Shows the dictionary of unique words and BoW vectors for each sentence.

BoW ignores grammar, word order, and punctuation but captures the overall word distribution.

Real-Time Applications:

Text Analytics: Finding word frequency in documents.

Information Retrieval: Searching documents based on keywords.

Recommendation Systems: Understanding text similarity between items or reviews.

Chatbots / NLP Systems: Preparing text data for ML models.

Steps to Run:

Install Gensim: python -m pip install gensim

Run the script: python gensim_word2vec.py'''