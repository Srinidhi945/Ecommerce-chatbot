## E-commerce AI Chatbot 🛍️🤖

This project is an intelligent, conversational AI chatbot designed to enhance the e-commerce shopping experience. It leverages a powerful RAG (Retrieval-Augmented Generation) pipeline, combining a vector database, conversational memory, and large language models to provide users with accurate, context-aware answers about products.

---

## 📚 Table of Contents

* [Features](#-features)
* [Tech Stack & Architecture](#-tech-stack--architecture)
* [Setup and Installation](#-setup-and-installation)
* [Configuration](#-configuration)
* [Running the Application](#-running-the-application)
* [Contact](#-contact)

---

## ✨ Features

* **Conversational Q&A**: Users can ask questions about products in natural language and receive coherent, helpful answers.
* **RAG Pipeline**: Utilizes LangChain to retrieve relevant product information from a vector database (Astra DB) before generating an answer, ensuring responses are factual and based on product data.
* **Persistent Memory**: Leverages Redis to remember the context of the conversation, allowing for follow-up questions and a more natural interaction.
* **Powered by Google Gemini**: Uses Google's powerful Large Language Models for intelligent and fluent response generation.
* **Simple Web Interface**: A clean and simple frontend built with Flask, HTML, and Bootstrap for easy interaction.

---

## 🛠️ Tech Stack & Architecture

This project integrates several modern technologies to create a robust AI pipeline.

* **Frontend**: `HTML`, `Bootstrap CSS`
* **Backend**: `Flask` (Python)
* **Orchestration Framework**: `LangChain`
* **Vector Database**: `DataStax Astra DB` (for storing and searching product embeddings)
* **Caching/Memory**: `Redis` (for caching and storing conversation history)
* **Embeddings Model**: `Hugging Face` Sentence-Transformers
* **LLM Provider**: `Google Gemini` (via `langchain-google-genai`)

## Application Flow
1.  A user sends a message through the HTML/Bootstrap frontend.
2.  The Flask backend receives the request.
3.  LangChain retrieves the recent conversation history from **Redis**.
4.  The user's query is converted into a vector embedding using **Hugging Face** models.
5.  LangChain performs a similarity search in **Astra DB** to find the most relevant product information (the "Retrieval" step).
6.  The retrieved context, conversation history, and the user's query are combined into a detailed prompt.
7.  This prompt is sent to the **Google Gemini** model to generate a response.
8.  The response is sent back to the user, and the new interaction is saved in Redis.

---

## ⚙️ Setup and Installation

Follow these steps carefully to set up the project locally.

### Prerequisites
* Python 3.8+
* Git
* An account with **DataStax Astra DB**.
* A **Google AI API Key** (for Gemini).
* A running **Redis** instance (either local or cloud-hosted).

### Step 1: Clone the Repository
```sh
git clone [https://github.com/Srinidhi945/Ecommerce-chatbot.git](https://github.com/Srinidhi945/Ecommerce-chatbot.git)
cd Ecommerce-chatbot
```
### Step 2: Set Up Python Environment
``` sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Step 3: Configure Environment Variables
This is the most critical step. You must provide your secret keys.

In the root directory of the project, create a file named .env.

Copy the format below into your .env file and fill it with your actual credentials.
``` sh
ASTRA_DB_API_ENDPOINT="your_astra_db_endpoint_here"
ASTRA_DB_APPLICATION_TOKEN="AstraCS:your_astra_db_token_here"
GOOGLE_API_KEY="your_google_ai_api_key_here"
REDIS_URL="your_redis_connection_url_here"
```
### Step 4: Install Dependencies & Resolve Conflicts
First, install the packages from requirements.txt. Then, run the specified upgrade commands to ensure version compatibility.

Install base requirements:
``` sh
pip install -r requirements.txt
```
Run upgrade commands to resolve conflicts:
``` sh
python -m pip install --upgrade pip
pip install -U sentence-transformers
pip install -U langchain-huggingface
pip install -U redis
pip install -U langchain-redis
``` 
Running the Application
Once the setup is complete, you can run the Flask web server.
# Make sure your virtual environment is activated
``` sh
python app.py
``` 
The application will start, typically on http://127.0.0.1:5000. Open this URL in your web browser to interact with the chatbot.

## 📞 Contact
LinkedIn Profile:www.linkedin.com/in/srinidhi-poreddy

Project Link: https://github.com/Srinidhi945/Ecommerce-chatbot
