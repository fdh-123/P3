import streamlit as st
import speech_recognition as sr

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Voice Bot", page_icon="🤖", layout="centered")

# App title
st.title("🎤 Voice Recognition Bot")
st.write("Click the button below to start speaking, and the bot will recognize your speech.")

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "No speech detected. Please try again."
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Could not request results. Please check your internet connection."

# Ensure set_page_config is the first Streamlit function
if __name__ == "__main__":
    # Button to start speech recognition
    if st.button("🎙 Start Listening"):
        with st.spinner("Listening..."):
            recognized_text = recognize_speech()
        st.success("Recognition Complete!")
        st.write(f"**You said:** {recognized_text}")
