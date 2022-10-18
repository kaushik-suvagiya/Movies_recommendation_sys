import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    names = []
    posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        posters.append(fetch_poster(movie_id))
        names.append(movies.iloc[i[0]].title)

    return names,posters

#import os
#filepath = '/Users/Kaushik/Desktop/Py Prog/mrs'
#if os.path.exists(filepath):
 #   file = open('/Users/Kaushik/Desktop/Py Prog/mrs/codedata.pkl', 'rb')
  #  codedata = pickle.load(file)
   # file.close()
#else:
 #   print("File not present at desired location")

st.header('Content Based Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Select/Type a movie which you like in the dropdown button",
    movie_list
)

if st.button('Recommended Movies'):
    names,posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
#pip install streamlit
#run this code in terminal 'streamlit run myapp.py'
#To generate libraries requirement file 'pip freeze >requirments.txt'