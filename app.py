cat > app.py << 'EOF'
import streamlit as st
from tmdb_api import search_movie, format_movie_info

st.title("Movie Info Chatbot")
st.caption("Ask me about any movie! Just type the title.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant" and msg.get("poster_url"):
            st.image(msg["poster_url"], width=200)
        st.markdown(msg["content"])

if prompt := st.chat_input("Type a movie title..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    movie = search_movie(prompt)
    if movie:
        reply, poster_url = format_movie_info(movie)
    else:
        reply = f"Sorry, I couldn't find anything for '{prompt}'. Try another title!"
        poster_url = None
    st.session_state.messages.append({"role": "assistant", "content": reply, "poster_url": poster_url})
    with st.chat_message("assistant"):
        if poster_url:
            st.image(poster_url, width=200)
        st.markdown(reply)
EOF