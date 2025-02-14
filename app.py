import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e1ec7c71d1395bf4676d055dc8df8da6&language=en-US".format(movie)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommend_movie=[]
    recommend_posters=[]
    for i in movies_list[1:6]:
        fetched_movieid= movies.iloc[i[0]].id
        recommend_posters.append(fetch_poster(fetched_movieid))
        recommend_movie.append(movies.iloc[i[0]].title)

    return recommend_movie, recommend_posters


movies_dict= pickle.load(open('movie_list.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name= st.selectbox(
'Select the Movie you want to watch',
movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])