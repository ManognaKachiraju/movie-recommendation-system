# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:08:30 2021

@author: Chandramouli
"""

import pickle
import streamlit as st
import requests

def recommend(movie):
    index = movies[movies['Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].Title)

    return recommended_movie_names

# Set background image
page_bg_img = '''
<style>
    .stApp {
        background-image: url("https://payload.cargocollective.com/1/11/367710/13568488/MOVIECLASSICSerikweb_2500_800.jpg");
        background-size: cover;
    }
</style>
'''

# Apply background image
st.markdown(page_bg_img, unsafe_allow_html=True)

# Header
st.markdown('# Movie Recommendation System')

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie selection dropdown
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Show recommendation button
if st.button('Show Recommendation'):
    # Get recommendations
    recommended_movie_names = recommend(selected_movie)
    
    # Display recommendations with images
    st.markdown('## Recommended Movies:')
    for i, movie_name in enumerate(recommended_movie_names, start=1):
        st.subheader(f"{i}. {movie_name}")
        
        # Fetch and display movie poster
        poster_url = get_movie_poster_url(movie_name)
        if poster_url:
            st.image(poster_url, caption=f"Poster for {movie_name}", use_column_width=True)
        else:
            st.warning("Poster not available")

# Function to get movie poster URL using external API (you can replace this with your own method)
def get_movie_poster_url(movie_name):
    # Use an external API to get the poster URL based on the movie name
    # Replace this with your own API or method to fetch movie posters
    api_url = f"http://api.example.com/poster?title={movie_name}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json().get('poster_url')
    else:
        return None
