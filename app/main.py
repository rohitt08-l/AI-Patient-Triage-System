import streamlit as st
import os
import sys

# Add src folder to path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from chatbot_engine import triage_chatbot_response

st.set_page_config(page_title="AI Patient Triage Chatbot", layout="wide")

st.title("AI Patient Triage Chatbot")
st.write("Describe your symptoms in natural language.")

user_input = st.text_area(
    "Enter your symptoms",
    placeholder="Example: I have chest pain and breathing issue"
)

if st.button("Analyze Symptoms", key="chatbot_btn"):
    response = triage_chatbot_response(user_input)

    st.subheader("Detected Symptoms")
    st.write(response["symptoms"])

    st.subheader("Triage Level")
    st.success(response["triage"])

    st.subheader("Recommendation")
    st.info(response["recommendation"])