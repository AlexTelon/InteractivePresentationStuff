# controller_app.py
import streamlit as st
from tinydb import TinyDB

# Initialize the database
db = TinyDB('db.json')
responses_table = db.table('responses')

# Initialize session state for reset confirmation
if "reset" not in st.session_state:
    st.session_state.reset = False

st.title("Controller")

# Button to reset responses
if st.button("Reset Responses"):
    responses_table.truncate()  # Clear all responses from the database
    st.session_state.reset = True  # Mark that a reset has been performed
    st.rerun()  # Rerun the script to update the UI

# Show success message only after rerun
if st.session_state.reset:
    st.success("Responses have been reset.")
    st.session_state.reset = False  # Reset the confirmation state
