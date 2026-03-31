import requests

API_KEY = "5ba70d355399491611d6e9f9ce0e5377"
BASE_URL = "https://api.themoviedb.org/3"

def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {"query": title, "api_key": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]
    return None

def format_movie_info(movie):
    return (
        f"🎬 **{movie['title']}** ({movie.get('release_date', 'N/A')[:4]})\n\n"
        f"⭐ Rating: {movie.get('vote_average', 'N/A')}/10\n\n"
        f"📖 {movie.get('overview', 'No description available.')}"
    )