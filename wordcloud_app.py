# wordcloud_app.py
import streamlit as st
from tinydb import TinyDB
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Initialize the database
db = TinyDB('db.json')
responses_table = db.table('responses')

st.title("Live Word Cloud")

# Inject HTML meta tag for auto-refresh
refresh_interval = 1  # Refresh interval in seconds
st.markdown(
    f"""
    <meta http-equiv="refresh" content="{refresh_interval}">
    """,
    unsafe_allow_html=True
)

# Fetch responses
responses = responses_table.all()
text = ' '.join([r['response'] for r in responses])

if text:
    # Generate a word cloud object
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        collocations=False,
        # font_path='DejaVuSans.ttf'  # Ensure this font supports Unicode
    ).generate(text)

    # Display the generated image
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)
else:
    st.write("No responses yet.")
