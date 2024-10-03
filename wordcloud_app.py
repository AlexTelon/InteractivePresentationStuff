# wordcloud_app.py
import streamlit as st
from tinydb import TinyDB, Query
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

st.title("Live Word Cloud")

# Display the active question
st.header(active_question)

# Auto-refresh using JavaScript
refresh_rate = 5000  # Refresh every 5000 milliseconds (5 seconds)
st.markdown(
    f"""
    <script>
    function refreshPage() {{
        setTimeout(function() {{
            window.location.reload();
        }}, {refresh_rate});
    }}
    window.onload = refreshPage;
    </script>
    """,
    unsafe_allow_html=True
)

# Fetch responses for the active question
responses = responses_table.search(Query().question == active_question)
text = ' '.join([r['response'] for r in responses])

if text:
    # Generate the word cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        collocations=False,
    ).generate(text)

    # Display the word cloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)
else:
    st.write("No responses yet.")
