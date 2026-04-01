import requests

url = "https://api.themoviedb.org/3/search/movie"
params = {"query": "Inception", "api_key": "ab7d78d61b543d4013e49d7d23a763c5"}
response = requests.get(url, params=params)   # <-- this is the API call
response.json()

import requests
import os

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {"query": title, "api_key": API_KEY}
    response = requests.get(url, params=params)   # This is the API call
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]   # Return the top matching result
    return None
def format_movie_info(movie):
    return (
        f"🎬 **{movie['title']}** ({movie.get('release_date', 'N/A')[:4]})\n\n"
        f"⭐ Rating: {movie.get('vote_average', 'N/A')}/10\n\n"
        f"📖 {movie.get('overview', 'No description available.')}"
    )

import streamlit as st
from tmdb_api import search_movie, format_movie_info

st.title("🎥 Movie Info Chatbot")
st.caption("Ask me about any movie! Just type the title.")
# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display the existing conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
# Handle new user input
if prompt := st.chat_input("Type a movie title..."):
    # Display and save the user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    # Call the API and generate a bot reply
    movie = search_movie(prompt)
    if movie:
        reply = format_movie_info(movie)
    else:
        reply = f"Sorry, I couldn't find anything for **'{prompt}'**. Try another title!"
    # Display and save the bot's reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
