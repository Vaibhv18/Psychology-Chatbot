# Psychology-Chatbot
This repository contains the implementation of a psychology chatbot that leverages both rule-based and generative AI models to provide responses to user queries. The project consists of two main components:

Model Training and Integration (Jupyter Notebook)
Web Application (Flask)
Overview
The psychology chatbot is designed to interact with users, providing responses based on predefined patterns and responses. When the predefined responses are not sufficient, the chatbot uses the Gemini API to generate appropriate responses.

Features
Rule-Based Responses: The chatbot uses a predefined set of patterns and responses stored in a JSON file.
Generative AI Integration: When the rule-based model cannot find a match, the chatbot queries the Gemini API for a response.
Web Interface: A Flask web application that allows users to interact with the chatbot through a simple web interface.
Repository Structure
model.ipynb: Jupyter Notebook for training the rule-based model and integrating it with the Gemini API.
app.py: Flask web application code for serving the chatbot.
intents.json: JSON file containing predefined patterns and responses for the rule-based model.
templates/: Folder containing HTML templates for the web application.
.env: Environment file for storing sensitive information like API keys (not included in the repository for security reasons).

Usage
Open the web application in your browser.
Interact with the chatbot by typing messages into the input box.
The chatbot will respond based on predefined patterns or generate a response using the Gemini API if no match is found.
Contribution
Feel free to fork this repository, create issues, or submit pull requests to contribute to the project.
