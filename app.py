import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Load the saved model from the file
file_name = 'knn_model.pkl'
with open(file_name, 'rb') as file:
    loaded_model = pickle.load(file)

# Load saved data
merged_df = pd.read_csv('merged_df.csv')
ratings_df = pd.read_csv('ratings.csv')

userIds = ratings_df['userId'].unique()
all_movies = set(merged_df['movieId'].values)

def recommend(user_id):
    """Generate movie recommendations for a given user ID.
    Parameters
    ----------
    user_id : int
        The ID of the user for whom recommendations are generated.

    Returns
    -------
    pd.DataFrame
        The top 10 recommended movies and the seen movies genres dataframe.
    """
    try:
        user_movies = ratings_df[ratings_df['userId'] == user_id]['movieId'].unique()
        unrated_movies = merged_df[~merged_df['movieId'].isin(user_movies)]

        # Get top-10 movie recommendations for the user
        k = 10
        user_recommendations = loaded_model.get_neighbors(user_id, k=k)
        recommended_movies = unrated_movies[unrated_movies['movieId'].isin(user_recommendations)]
        
        return recommended_movies

    except ValueError as e:
        st.error(str(e))
        return pd.DataFrame(), pd.DataFrame()


####################################################################
# streamlit
##################################################################

# Set page title and favicon
st.set_page_config(page_title="Movies Recommender", page_icon=":clapper:")

# Header
st.title('Movies Recommendation System')
st.write('A Collaborative Filtering Based Recommender System')

# Display an image
st.image(
    "https://res.cloudinary.com/practicaldev/image/fetch/s--hGvhAGUu--/c_imagga_scale,f_auto,fl_progressive,"
    "h_500,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/mih10uhu1464fx1kr0by.jpg",
    use_column_width=True
)

# User input
st.subheader('Select a User ID')
userId = st.selectbox("Choose a User ID", userIds)

if st.button('Show Recommendations'):
    recommended_movies = recommend(userId)
    if recommended_movies.empty:
        st.write("No movie recommendations found for this user.")
    else:
        # Display recommended movies
        st.subheader('Top Recommended Movies')
        for index, movie in recommended_movies.iterrows():
            st.image(movie['img_url'], caption=movie['title'], width=100)
            st.write(f"**Title:** {movie['title']}")

# Add some footer text
st.markdown("---")
st.write("Created by Emuejevoke Eshemitan")