import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import json
import random
import string

# Loadng the intents data from the intents.json
with open('intents.json', 'r') as file:
    data = json.load(file)

    # Initializing lemmatizer and creating a set of stopwords
nltk.download('stopwords') 
lemmatizer = WordNetLemmatizer()
stop_words = set(nltk.corpus.stopwords.words('english'))

# Function to preprocess the text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    tokens = nltk.word_tokenize(text)
    # Remove punctuation and lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum()]
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Creating a dictionary to hold the patterns and their corresponding tags
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
patterns_dict = {}
for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns_dict[tuple(preprocess_text(pattern))] = intent['tag']

# Creating a dictionary to hold the responses and their corresponding tags
responses_dict = {}
for intent in data['intents']:
    responses_dict[intent['tag']] = intent['responses']

    # Function to get a response from the chatbot
def get_response(user_input):
    user_input = preprocess_text(user_input)
    for pattern, tag in patterns_dict.items():
        if set(user_input).intersection(set(pattern)):
            return random.choice(responses_dict[tag])
    return "I'm sorry, I don't understand."

import joblib

# Saving the model using joblib
joblib.dump((patterns_dict, responses_dict), 'psychology_chatbot_model.joblib')