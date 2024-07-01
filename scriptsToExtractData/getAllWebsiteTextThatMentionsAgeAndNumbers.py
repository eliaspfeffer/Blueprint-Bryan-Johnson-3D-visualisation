import requests
from bs4 import BeautifulSoup
import re

# How to use this script: 
# Run it and then let ChatGPT extract all variables that are mentioned in the text.

# Function to fetch and parse the webpage content
def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to find sentences with the keyword "age" followed by a number
def find_age_sentences(content):
    sentences = []
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    
    # Split text into sentences
    potential_sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    
    # Regular expression to find "age" followed by a number
    age_pattern = re.compile(r'\bage\b.*?\b(\d+)\b|\b(\d+)\b.*?\bage\b', re.IGNORECASE)
    
    for sentence in potential_sentences:
        if age_pattern.search(sentence):
            sentences.append(sentence.strip())
    
    return sentences

# URL of the webpage
url = "https://protocol.bryanjohnson.com/"

# Fetch and process the webpage
content = fetch_webpage(url)
if content:
    age_sentences = find_age_sentences(content)
    for sentence in age_sentences:
        print(sentence)
else:
    print("Failed to fetch the webpage.")
