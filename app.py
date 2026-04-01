import streamlit as st
from tmdb_api import search_movie, format_movie_info

st.title("🎥 Movie Info Chatbot")
st.caption("Ask me about any movie! Just type the title.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant" and msg.get("poster_url"):
            st.image(msg["poster_url"], width=200)
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type a movie title..."):
    # Save and display user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Search movie
    movie = search_movie(prompt)

    if movie:
        reply, poster_url = format_movie_info(movie)
    else:
        reply = f"Sorry, I couldn't find anything for *'{prompt}'*. Try another title!"
        poster_url = None

    # Save assistant message including poster
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply,
        "poster_url": poster_url
    })

    # Display assistant message with poster
    with st.chat_message("assistant"):
        if poster_url:
            st.image(poster_url, width=200)
        st.markdown(reply)