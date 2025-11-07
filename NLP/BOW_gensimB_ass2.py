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

'''Explanation:

Introduction:

Bag of Words (BoW) is a technique in Natural Language Processing (NLP) that represents text as numerical vectors based on word frequency.

TF-IDF (Term Frequency-Inverse Document Frequency) is another technique that gives importance to unique words in a document and reduces the weight of common words.

These techniques are widely used in text analytics, search engines, recommendation systems, and NLP tasks.

Tokenization:

The text is split into individual words (tokens) using split() in the first method (tokens2) and simple_preprocess() in the second method (text3).

Tokenization helps in processing each word individually for analysis.

Dictionary Creation:

corpora.Dictionary() is used to map each unique token to a unique ID.

Example from output: 'I': 0, 'Python': 1, 'programming': 9

This dictionary acts as a reference for creating vector representations of sentences.

Bag of Words (BoW) Representation:

doc2bow() converts each sentence into a list of tuples (word_id, frequency) representing how many times each word occurs.

Example: [(0, 1), (6, 1), (9, 1)] → Word IDs 0, 6, 9 appear once in the sentence.

BoW ignores grammar and word order but captures word occurrence information.

Output Interpretation:

The first method shows BoW using simple split(), which may include punctuation in tokens.

The second method uses simple_preprocess() which removes punctuation and converts words to lowercase, producing a cleaner dictionary and BoW vectors.

Example output shows tokenized dictionary and frequency counts for each sentence.

Real-Time Applications:

Text Analytics: Analyze word frequency in articles, reviews, or social media posts.

Information Retrieval: Search documents or match keywords efficiently.

Recommendation Systems: Measure similarity between documents based on word occurrence.

Chatbots / NLP Models: Preprocess text for machine learning and AI applications.

Steps to Run:

Install Gensim library: python -m pip install gensim

Save the script (e.g., gensim_bow.py) and run it using: python gensim_bow.py'''

# Upgrade pip (optional but recommended)
# python -m pip install --upgrade pip

# # Install SpaCy for NLP tasks
# python -m pip install spacy

# # Download English language model for SpaCy
# python -m spacy download en_core_web_sm

# # Install Gensim for Bag of Words and TF-IDF
# python -m pip install gensim

# # Install NumPy (required by Gensim)
# python -m pip install numpy

# # Optional: Install pandas for handling text data (useful for future NLP tasks)
# python -m pip install pandas

# # Optional: Install matplotlib and seaborn for visualizations
# python -m pip install matplotlib seaborn
