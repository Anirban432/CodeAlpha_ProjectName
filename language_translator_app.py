import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import tempfile

# Set up page
st.set_page_config(page_title="Language Translation Tool", layout="centered")
st.title("🌍 Language Translation Tool")

# Translator instance
translator = Translator()

# Input text
text_input = st.text_area("Enter text to translate", height=150)

# Language options
languages = list(LANGUAGES.values())
lang_codes = list(LANGUAGES.keys())

# Language selection
source_lang = st.selectbox("Select source language", languages, index=languages.index("english"))
target_lang = st.selectbox("Select target language", languages, index=languages.index("hindi"))

# --- BUTTON ---
translate_clicked = st.button("Translate", key="unique_translate_button")

# --- LOGIC ---
if translate_clicked:
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text before translating.")
    else:
        try:
            src_code = lang_codes[languages.index(source_lang)]
            tgt_code = lang_codes[languages.index(target_lang)]

            translated = translator.translate(text_input, src=src_code, dest=tgt_code)

            st.success("✅ Translation successful!")
            st.subheader("Translated Text:")
            st.text_area("Output", translated.text, height=150)

            # Text-to-speech
            tts = gTTS(text=translated.text, lang=tgt_code)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tts.save(tmp.name)
                st.audio(tmp.name, format="audio/mp3")

        except Exception as e:
            st.error(f"❌ Translation failed: {e}")
