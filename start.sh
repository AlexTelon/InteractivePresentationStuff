#!/bin/bash

# Start the user input interface
echo "Starting the user input interface on port 8501..."
streamlit run app.py --server.port=8501 &

# Start the word cloud display
echo "Starting the word cloud display on port 8502..."
streamlit run wordcloud_app.py --server.port=8502 &

# Start the controller interface
echo "Starting the controller interface on port 8503..."
streamlit run controller_app.py --server.port=8503 &

# Wait for all background processes to complete
wait
