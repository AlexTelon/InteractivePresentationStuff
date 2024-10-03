import streamlit as st
from tinydb import TinyDB

# Initialize the database
db = TinyDB('db.json')
responses_table = db.table('responses')

# Initialize session state for storing responses
if "submitted" not in st.session_state:
    st.session_state.submitted = False

st.title("Conference Interactive Word Cloud")

# Display the current question
question = "What is your favorite programming language?"
st.header(question)

# User input
response = st.text_input("Your response here (emojis supported):")

if st.button("Submit"):
    if response.strip():
        responses_table.insert({'response': response.strip()})
        st.session_state.submitted = True  # Mark that a response was submitted
        st.rerun()  # Rerun the script to refresh the UI
    else:
        st.error("Please enter a response.")

# Show success message only after rerun
if st.session_state.submitted:
    st.success("Thank you for your response!")
    st.session_state.submitted = False  # Reset submission state
