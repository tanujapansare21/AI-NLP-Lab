###  Assignment No 5 ###

"""Assignment Title :  Implement regular expression function to find URL, IP address, Date,
PAN number in textual data using python libraries"""


import spacy
import re

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Define regular expressions
url_pattern = re.compile(r'https?://\S+|www\.\S+')

ip_address_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
pan_number_pattern = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')

def extract_entities(text):
    # Tokenize the text using spaCy
    doc = nlp(text)

    # Find entities using regular expressions
    urls = re.findall(url_pattern, text)
    ip_addresses = re.findall(ip_address_pattern, text)
    dates = re.findall(date_pattern, text)
    pan_numbers = re.findall(pan_number_pattern, text)

    # Extract spaCy entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return {
        'urls': urls,
        'ip_addresses': ip_addresses,
        'dates': dates,
        'pan_numbers': pan_numbers,
        'spaCy_entities': entities
    }


# Example usage
text_data = """
Here is a sample text with a URL: https://www.Sample.com. 
Also, an IP address: 192.168.789.102. 
The date is 2023-01-01.
A PAN number is BBRPL4574H.
"""

results = extract_entities(text_data)

print("URLs:", results['urls'])
print("IP Addresses:", results['ip_addresses'])
print("Dates:", results['dates'])
print("PAN Numbers:", results['pan_numbers'])
print("Entities:", results['spaCy_entities'])


'''
**************   OUTPUT     ****************

URLs: ['https://www.Sample.com.']
IP Addresses: ['192.168.789.102']
Dates: ['2023-01-01']
PAN Numbers: ['BBRPL4574H']
Entities: [('IP', 'ORG'), ('192.168.789.102', 'CARDINAL'), ('2023-01-01', 'DATE'), ('PAN', 'ORG')]

'''
'''📝 Assignment No. 05 – Explanation
Title:

Implement Regular Expression functions to find URL, IP Address, Date, PAN Number in textual data using Python libraries

✅ Code Explanation (Line-by-Line)
Code Line	Explanation
import spacy	Imports SpaCy library for NLP processing
import re	Imports re module used for Regular Expressions
nlp = spacy.load("en_core_web_sm")	Loads the English language model to detect named entities
url_pattern = re.compile(...)	Regular expression to find URLs starting with http, https, or www
ip_address_pattern = re.compile(...)	Regex to find IP addresses in the format x.x.x.x
date_pattern = re.compile(...)	Regex to find dates in format YYYY-MM-DD
pan_number_pattern = re.compile(...)	Regex to find Indian PAN numbers (ABCDE1234F)
def extract_entities(text):	Function to extract entities from given text
doc = nlp(text)	Converts raw text into SpaCy document for entity detection
urls = re.findall(url_pattern, text)	Finds all URLs in the text
ip_addresses = re.findall(ip_address_pattern, text)	Extracts all IP addresses
dates = re.findall(date_pattern, text)	Extracts all dates
pan_numbers = re.findall(pan_number_pattern, text)	Extracts all PAN numbers
entities = [(ent.text, ent.label_) for ent in doc.ents]	Extracts named entities detected by SpaCy
return {...}	Returns results in dictionary format
text_data = """ ... """	Sample input text to test the program
results = extract_entities(text_data)	Calls the function to extract all entities
print(...)	Prints extracted URLs, IPs, dates, PAN, and SpaCy entities
🧪 Output Explanation
Output Element	Meaning
URLs	All website links detected using regex
IP Addresses	Extracted IP address from text
Dates	Extracted valid date formats
PAN Numbers	Extracted valid PAN Card numbers
Entities	SpaCy detected named entities like ORG, DATE, CARDINAL, etc.
Example Output Breakdown:
URLs: ['https://www.Sample.com.']  
→ URL present in the text

IP Addresses: ['192.168.789.102']  
→ Extracted as IP (even though invalid logically, regex still matches)

Dates: ['2023-01-01']  
→ Correctly identified date

PAN Numbers: ['BBRPL4574H']  
→ Detected valid PAN format

Entities: [('IP', 'ORG'), ('192.168.789.102', 'CARDINAL'), ('2023-01-01', 'DATE'), ('PAN', 'ORG')]  
→ SpaCy tagged IP as ORG, date as DATE, etc.'''