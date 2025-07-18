import streamlit as st

st.title("Simple Dummy AI")

user_input = st.text_input("You:", "")

responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm just code, but I'm fine!",
    "x": "You typed X.",
    "y": "You typed Y.",
    "z": "You typed Z."
}

if user_input:
    reply = responses.get(user_input.lower(), "Sorry, I don't understand.")
    st.text(f"AI: {reply}")
