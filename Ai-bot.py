import streamlit as st
from gtts import gTTS
import wikipedia
import pyjokes
import time
import io
import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import datetime
import os
import speech_recognition as sr
recognizer = sr.Recognizer()

# UI Configuration
st.set_page_config('Voice Bot', "🤖", initial_sidebar_state="expanded", layout="centered")

# Page Title
st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        color: White;
        font-family: "Lucida Console";
        white-space: nowrap;
    }
    </style>
    <h1 class="centered-title"><b>VOICE BOT</b></h1>
""", unsafe_allow_html=True)

# Image Display
image_path =r"C:\Users\hp\Desktop\render-demo\bot_image.png"
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning("⚠️ Bot image not found! Please check the file path.")

st.sidebar.info("To use voice features, please allow microphone access when prompted by your browser.")    

st.sidebar.header("User Guide")
st.sidebar.markdown("""
### **How to Use:**
1. **Start Chatting:**
   - Record your audio and click **"Run Bot"**.

2. **Voice Commands Examples:**
   - "What is the time?" for current time.
   - "Tell me a joke." for fun.
   - "Search for [topic]" for Wikipedia search.
   - "Open Google" or "Open YouTube" to browse.

3. **Exit Chat:**
   - Say "Exit" or "Bye" to end.
---
""", unsafe_allow_html=True)

# Initialize Recognizer
recognizer = Recognizer()

# Text-to-Speech Function
def text_speech(text):
    tts = gTTS(text=text, lang='en')
    speech_bytes = io.BytesIO()
    tts.write_to_fp(speech_bytes)
    speech_bytes.seek(0)
    return speech_bytes

# Audio Capture & Transcription
def takeCommand(audio_file):
    if audio_file:
        st.write("Audio Recorded.")
        audio_bytes = audio_file.getvalue()
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_bytes)
        with AudioFile("temp_audio.wav") as source:
            audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='en-in')
            return text
        except Exception:
            st.error("Error: Unable to transcribe the audio. Please try again")
            return ""

st.success("✅ Streamlit App Loaded Successfully!")
