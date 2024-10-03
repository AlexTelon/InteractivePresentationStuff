# app.py
import streamlit as st
from tinydb import TinyDB, Query

# Initialize the database
db = TinyDB('db.json')
responses_table = db.table('responses')
config_table = db.table('config')

# Get the active question from the database
active_question_record = config_table.get(doc_id=1)
if active_question_record:
    active_question = active_question_record['question']
else:
    st.error("No active question set.")
    st.stop()

st.title("Conference Interactive Word Cloud")

# Display the current active question
st.header(active_question)

# Inform users to refresh the page if the question changes
st.info("If the question changes, please refresh this page.")

# User input
response = st.text_input("Your response here (emojis supported):")

if st.button("Submit"):
    if response.strip():
        responses_table.insert({'question': active_question, 'response': response.strip()})
        st.success("Thank you for your response!")
        # Clear the input field
        st.rerun()
    else:
        st.error("Please enter a response.")
