# 🎬 Movie Recommender System
This repository contains a content-based Movie Recommender System built using Python. The system analyzes movie metadata, processes textual information, and applies machine learning techniques to recommend similar movies based on user input. It is designed to provide personalized movie recommendations using CountVectorizer for text vectorization and Cosine Similarity for measuring content similarity.

# 📌 Project Overview
The Movie Recommender System follows a content-based filtering approach, meaning it recommends movies similar to a given input movie by analyzing textual attributes like title, genre, keywords, and other metadata.

The project consists of two main components:

## Backend (Recommendation Engine)

- Data preprocessing: Cleaning and transforming the dataset
- Tag creation: Combining important features to form a meaningful representation of each movie
- Text vectorization using CountVectorizer
- Cosine Similarity computation to determine how closely related two movies are
- Generating the top 5 similar movie recommendations based on the input movie

## Frontend (User Interface using Streamlit)

- An interactive UI built with Streamlit
- User-friendly search and recommendation display
- Seamless integration with the backend to provide real-time recommendations

# 🛠️ Technologies Used
- Python: Core programming language
- Pandas: Data preprocessing and manipulation
- Numpy: Efficient numerical operations
- Scikit-learn: Machine learning tools for vectorization and similarity calculations
- CountVectorizer: NLP technique for feature extraction
- Cosine Similarity: Computes similarity scores between movie vectors
- Streamlit: Lightweight framework for deploying an interactive UI

# 🎯 How It Works
- The dataset containing movie information is preprocessed by cleaning missing values and merging relevant features into a single tag.
- The system converts these tags into numerical vectors using CountVectorizer.
- The Cosine Similarity score is calculated between movies to find the most similar ones.
- The user inputs a movie title through the Streamlit interface.
- The system retrieves and displays the top 5 most similar movies based on the similarity scores.


## 📂 Dataset  


The dataset used in this project can be found [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
