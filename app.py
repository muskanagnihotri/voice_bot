import streamlit as st
from query_handler import handle_query
import pyttsx3

# Text-to-Speech setup
engine = pyttsx3.init()

def speak(text):
    """Speak the provided text."""
    try:
        print("Speaking:", text)  # Debug print
        engine.say(text)
        engine.runAndWait()  # Ensures the speech is fully processed and played
    except RuntimeError:
        # Handle the run loop already started issue
        print("Error: Unable to speak.")
# Streamlit interface
st.title("Online Shopping Assistant Bot")
st.write("Ask me anything about shopping!")

# Input box
user_input = st.text_input("Your Query:")

if user_input:
    response = handle_query(user_input)
    st.write(f"Bot: {response}")
    speak(response)
