TRANSLINGUA: AI-Powered Language Translator

1)TransLingua is a simple and interactive multi-language translation web application built using Streamlit.  
2)It uses Google Gemini AI for smart contextual translation and automatically falls back to Google Translator if API quota is unavailable.

working demo:
https://drive.google.com/file/d/1nOAn2ZQNXvk51vaQe1mSoOyE0sS0JziK/view?usp=sharing

🚀Features:

Multi-language translation (English, Hindi, Telugu, Tamil, Spanish, French, German, Chinese, Japanese, Korean)
AI-powered translation using **Google Gemini API**
Automatic fallback using **GoogleTranslator** (deep-translator)
Clean Streamlit UI
Real-time translation
Smart error handling


🛠️ Technologies Used:

- Python
- Streamlit
- Google Generative AI (Gemini API)
- Deep Translator
- Python Dotenv

📁 Project Structure

translingua/
│
├── translang.py # Main application file
├── .env # API key (not shared)
├── requirements.txt # Required libraries
└── README.md

🔑 API Key Setup (Gemini AI)

1. Go to: https://aistudio.google.com/
2. Click **Get API Key**
3. Create a new API key
4. Create a `.env` file in your project folder

Add:
GOOGLE_API_KEY=your_api_key_here

Install required libraries:
pip install streamlit google-generativeai python-dotenv deep-translator

How to Run
streamlit run translang.py

Then open:
http://localhost:8501


🧠How It Works:

User enters text
Select source and target languages
App tries translation using Gemini AI
If quota/API fails → automatically switches to Google Translator
Translated text is displayed instantly

🎯Project Objective:

This project demonstrates how AI APIs can be integrated with web applications to build practical tools that help break language barriers.
