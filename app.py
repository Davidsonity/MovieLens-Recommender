import pandas as pd
import numpy as np
import streamlit as st
# from st_clickable_images import clickable_images

# Load saved date
profiles_df = pd.read_csv('profiles.csv')
movies_genres_df = pd.read_csv('movies_genres.csv')
users_df = pd.read_csv('ratings.csv')

userIds = users_df['userId'].unique()

all_movies = set(movies_genres_df['movieId'].values)


def paginator(label, items, items_per_page=10, on_sidebar=True):
    """Lets the user paginate a set of items.
    Parameters
    ----------
    label : str
        The label to display over the pagination widget.
    items : Iterator[Any]
        The items to display in the paginator.
    items_per_page: int
        The number of items to display per page.
    on_sidebar: bool
        Whether to display the paginator widget on the sidebar.

    Returns
    -------
    Iterator[Tuple[int, Any]]
        An iterator over *only the items on that page*, including
        the item's index."""

    # Figure out where to display the paginator
    if on_sidebar:
        location = st.sidebar.empty()
    else:
        location = st.empty()

    # Display a pagination selectbox in the specified location.
    items = list(items)
    n_pages = len(items)
    n_pages = (len(items) - 1) // items_per_page + 1
    page_format_func = lambda i: "Page %s" % i
    page_number = location.selectbox(label, range(n_pages), format_func=page_format_func)

    # Iterate over the items in the page to let the user display them.
    min_index = page_number * items_per_page
    max_index = min_index + items_per_page
    import itertools
    return itertools.islice(enumerate(items), min_index, max_index)


def generate_score(user_id):
    # get user profile
    user_profile = profiles_df[profiles_df['userId'] == user_id]

    # Now let's get the test user vector by excluding the `user` column
    user_vector = user_profile.iloc[0, 1:].values

    # Get watched movies
    watched_movies = users_df[users_df['userId'] == user_id]['movieId'].to_list()
    watched_movies = set(watched_movies)

    # Get seen movies df
    seen_movies_genres = movies_genres_df[movies_genres_df['movieId'].isin(watched_movies)]
    seen_movies_genres = seen_movies_genres[['movieId', 'title']]

    # Reset Index
    seen_movies_genres = seen_movies_genres.reset_index(drop=True)

    # Get unseen movies
    unseen_movies = all_movies.difference(watched_movies)

    # Get genre vectors of unseen movies
    unseen_movies_genres = movies_genres_df[movies_genres_df['movieId'].isin(unseen_movies)]

    # Now let's get the movie matrix by excluding `movieId` and `title` columns:
    movie_matrix = unseen_movies_genres.iloc[:, 4:].values

    # user np.dot() to get the recommendation scores for each movie
    scores = np.dot(movie_matrix, user_vector)

    # Get unseen dataframe
    unseen_df = unseen_movies_genres[['movieId', 'title', 'img_url', 'url']]

    # load scores column to unseen dataframe
    unseen_df['score'] = pd.Series(scores)

    # Sort by score columns
    unseen_df = unseen_df.sort_values(by=['score'], ascending=False)
    # Reset index
    unseen_df = unseen_df.reset_index(drop=True)

    # Return dataframe
    return unseen_df[:20], seen_movies_genres


####################################################################
# streamlit
##################################################################

st.header('Movies Recommendation System ')

st.markdown('> A Content-based Movies Recommender System Using User Profile and Movie Genres')

st.image(
    "https://res.cloudinary.com/practicaldev/image/fetch/s--hGvhAGUu--/c_imagga_scale,f_auto,fl_progressive,"
    "h_500,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/mih10uhu1464fx1kr0by.jpg "
)

# Use side bar
st.sidebar.header('User Profile')

# Select a user id
userId = st.sidebar.selectbox(
    "Enter User Id", userIds
)

if st.sidebar.button('Show Recommendations'):
    recommended_movies, seen_movies = generate_score(userId)
    # Get links
    link = list(recommended_movies['img_url'].values)
    title = list(recommended_movies['title'].values)
    st.subheader('Top 20 recommended movies')
    st.image(
        link, caption=title, width=100
    )
    #
    # sunset_imgs = link
    #
    # image_iterator = paginator("Select a sunset page", sunset_imgs)
    # indices_on_page, images_on_page = map(list, zip(*image_iterator))
    # st.image(images_on_page, width=100, caption=title)
    # st.subheader('Recommended Movies')

    # clicked = clickable_images(
    #     link,
    #     titles=title,
    #     div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    #     img_style={"margin": "5px", "height": "200px"},
    # )
