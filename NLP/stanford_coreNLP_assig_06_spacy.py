###  Assignment No 6 ###

"""Assignment Title : : Implement and visualize Dependency Parsing of Textual Input
using Stan- ford CoreNLP and Spacy library"""


import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
Earth is the third planet from the Sun in our solar system and the only known celestial body to support life. 
With a diverse range of ecosystems, it is home to a vast array of plant and animal species, including humans. 
Earth's atmosphere, composed mainly of nitrogen and oxygen, sustains life by providing the necessary conditions for biological processes to thrive.
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")

# how to run:http://localhost:5000
'''Explanation:

Introduction:

Dependency Parsing is a Natural Language Processing (NLP) task that identifies grammatical relationships between words in a sentence.

It helps in understanding sentence structure, such as which word is the subject, object, or modifier of another word.

Applications include chatbots, information extraction, question answering, and text summarization.

Importing Libraries:

spaCy is used for NLP tasks like tokenization, POS tagging, NER, and dependency parsing.

displacy is SpaCy’s visualization tool to display dependency trees.

Loading the Language Model:

nlp = spacy.load("en_core_web_sm")


Loads a pre-trained English model for analyzing text.

Processing Text:

multiline_doc = nlp(multiline_text) processes the input text into tokens.

Each word is analyzed for its part-of-speech, head word, and dependency relation.

Printing Token Details:

for token in multiline_doc:
    print(token.text, token.tag_, token.head.text, token.dep_)


token.text: The word itself.

token.tag_: Part-of-speech tag (e.g., NN, VBZ).

token.head.text: The word it is dependent on.

token.dep_: Type of grammatical relationship (e.g., nsubj = subject, dobj = object).

Example:

TOKEN: Earth
token.tag_ = NNP
token.head.text = is
token.dep_ = nsubj


Visualization:

displacy.serve(multiline_doc, style="dep")


Opens a browser window showing a dependency tree with arrows indicating relationships.

Helps visually understand sentence structure.

Real-Time Applications:

Chatbots / Virtual Assistants: Understand intent and meaning.

Information Extraction: Identify subject-object-action relationships.

Text Summarization & Question Answering: Analyze sentence structure to generate answers or summaries.

Steps to Run from Scratch:

# Upgrade pip (optional)
python -m pip install --upgrade pip

# Install SpaCy library
python -m pip install spacy

# Download the English language model
python -m spacy download en_core_web_sm


✅ Note:

Dependency parsing is essential for machines to understand grammar and word relationships.

displacy provides a visual representation that makes it easier to analyze complex sentences.'''