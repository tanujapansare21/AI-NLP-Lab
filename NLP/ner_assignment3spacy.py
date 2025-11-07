###  Assignment No 3 ###

#Assignment Title : Name Entity Recognition in python with spacy


import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text using SpaCy
    doc = nlp(text)
    
    # Extract named entities and their labels
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

if __name__ == "__main__":
    # Example text
    text = "Earth is the third planet from the Sun in our solar system and the only known celestial body to support life. With a diverse range of ecosystems, it is home to a vast array of plant and animal species, including humans."

    # Perform Named Entity Recognition
    named_entities = perform_ner(text)

    # Print the results
    print("Named Entities:")
    for entity, label in named_entities:
        print(f"{entity} - {label}")


'''
**************    OUTPUT

Named Entities:
Earth - LOC
third - ORDINAL
Sun - ORG

'''
'''
Explanation:

Introduction:

Named Entity Recognition (NER) is a Natural Language Processing (NLP) task that identifies named entities in text such as locations, organizations, dates, numbers, and people.

NER is widely used in information extraction, chatbots, search engines, and text analytics.

Importing Libraries:

spaCy is used for NLP tasks including tokenization, POS tagging, and NER.

Loading the Language Model:

nlp = spacy.load("en_core_web_sm") loads a pre-trained English model for processing text.

Function perform_ner(text):

Processes the input text using the SpaCy NLP pipeline.

Extracts named entities and their labels (like LOC = location, ORG = organization, PERSON = person, ORDINAL = order numbers).

Returns a list of tuples containing the entity and its label.

Example Text:

"Earth is the third planet from the Sun ..."

NER identifies:

Earth - LOC
third - ORDINAL
Sun - ORG


This shows the text is analyzed for entities like locations, numbers, and organizations.

Real-Time Applications:

Search engines: Identify key entities to improve search relevance.

Chatbots / Virtual Assistants: Understand names, places, and organizations in user queries.

Text Analytics: Extract meaningful information from large documents or social media.

Commands to Run from Scratch:

# Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

# Install SpaCy library
python -m pip install spacy

# Download the English language model for SpaCy
python -m spacy download en_core_web_sm

# Save the Python script (e.g., ner_spacy.py) and run it
python ner_spacy.py'''