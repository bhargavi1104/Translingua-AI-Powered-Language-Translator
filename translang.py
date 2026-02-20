
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title=" TRANSLINGUA:AI-Powered Language Translator",
    page_icon="🌍"
)
st.markdown("""
<style>
.block-container {
    padding-top: 1.6rem !important;
}
</style>
""", unsafe_allow_html=True)

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)


st.markdown(
    "<h2 style='text-align:center;'>🌍 AI-POWERED LANGUAGE TRANSLATOR</h2>",
    unsafe_allow_html=True
)

languages = [
    "english","hindi","telugu","tamil",
    "spanish","french","german",
    "chinese","japanese","korean"
]

text = st.text_area("📝 Enter text to translate:")
source_language = st.selectbox("🌐 Source Language:", languages)
target_language = st.selectbox("🌐 Target Language:", languages, index=1)


def translate_text(text, source_lang, target_lang):

    if API_KEY:
        try:
            model = genai.GenerativeModel("gemini-2.0-flash")

            prompt = f"""
            Translate this text from {source_lang} to {target_lang}:

            {text}

            Only return translated text.
            """

            response = model.generate_content(prompt)
            return response.text, "Gemini AI"

        except Exception:
            pass  

    try:
        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        return translated, "Google Translator (Fallback)"

    except Exception as e:
        return f"Error: {e}", "None"

if st.button("🔄 Translate"):

    if not text:
        st.warning("⚠️ Please enter text.")
    elif source_language == target_language:
        st.warning("⚠️ Same language selected.")
    else:
        with st.spinner("Translating..."):
            result, engine = translate_text(
                text,
                source_language,
                target_language
            )
      
        st.text_area("📌 Translated Text:", result, height=100)   