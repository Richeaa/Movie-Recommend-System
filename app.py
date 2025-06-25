import streamlit as st
import os
from dotenv import load_dotenv
import pickle
import requests
import gdown

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

file_id = '16kHA3XYnQXA3FI6zJ1zB15_mUjjOAYyG'  
output = 'similarity.pkl'

if not os.path.exists(output):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output, quiet=False)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

movies = pickle.load(open('movie.pkl', 'rb'))

movies_title = movies['title'].values


def fetch_poster(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return "https://via.placeholder.com/300x450?text=No+Image"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]

    recommend_posters = []
    recommend_movies = []
    for i in movies_list:
        title = movies.iloc[i[0]]['title']
        recommend_movies.append(title)
        recommend_posters.append(fetch_poster(title))
    return recommend_movies, recommend_posters

st.markdown("<h2 style='text-align: center;'>Movie Recommender System </h2>", unsafe_allow_html=True)

selected_movie = st.selectbox('Select a movie:', movies_title)

if st.button('Recommend'):
    movies, posters = recommend(selected_movie)

    st.markdown("Recommended Movies:")
    st.write("")  
    
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.text(movies[i])