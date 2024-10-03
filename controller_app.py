# controller_app.py
import streamlit as st
from tinydb import TinyDB, Query
import json

# Initialize the database
db = TinyDB('db.json')
responses_table = db.table('responses')
config_table = db.table('config')

# Load questions from the config file
with open('questions.json', 'r') as f:
    questions = json.load(f)

# Initialize session state for the active question
if "active_question" not in st.session_state:
    # Try to get the active question from the database
    active_question_record = config_table.get(Query().name == 'active_question')
    if active_question_record:
        st.session_state.active_question = active_question_record['question']
    else:
        st.session_state.active_question = questions[0]  # Default to the first question
        config_table.upsert({'name': 'active_question', 'question': st.session_state.active_question}, Query().name == 'active_question')

st.title("Controller")

# Display and select the active question
st.subheader("Select Active Question")
selected_question = st.selectbox(
    "Questions",
    questions,
    index=questions.index(st.session_state.active_question)
)

if st.button("Set Active Question"):
    st.session_state.active_question = selected_question
    config_table.upsert({'name': 'active_question', 'question': st.session_state.active_question}, Query().name == 'active_question')
    st.success(f"Active question set to: {st.session_state.active_question}")

# Button to reset responses for the active question
st.subheader("Reset Responses")
if st.button("Reset Responses for Active Question"):
    # Remove responses associated with the active question
    responses_table.remove(Query().question == st.session_state.active_question)
    st.success("Responses for the active question have been reset.")

# Optional: Reset all responses
if st.button("Reset All Responses"):
    responses_table.truncate()
    st.success("All responses have been reset.")
