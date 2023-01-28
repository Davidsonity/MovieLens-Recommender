# Content-based Movies Recommender System Using User Profile and Movie Genres

<center>
    <img src= "https://res.cloudinary.com/practicaldev/image/fetch/s--hGvhAGUu--/c_imagga_scale,f_auto,fl_progressive,h_500,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/mih10uhu1464fx1kr0by.jpg" width="800" alt="cognitiveclass.ai logo" />
</center>

> Deployment Site @ https://davidsonity-grouplens-movies-recommender-app-m9dj9x.streamlitapp.com/
>
> View Notebook @ https://github.com/Davidsonity/GroupLens-Movies-Recommender/blob/main/notebook.ipynb

## INTRODUCTION
The most common type of content-based recommendation system is to recommend items to users based on their profiles. The user's profile revolves around that user's preferences and tastes. It is shaped based on user ratings, including the number of times a user has clicked on different items or liked those items.

The recommendation process is based on the similarity between those items. The similarity or closeness of items is measured based on the similarity in the content of those items. When we say content, we're talking about things like the item's category, tag, genre, and so on. Essentially the features about an item.

### Objectives
The following are the main objectives of this project:
- Build a movies recommendation system for unique users using User Profile and Movie Genres

### Steps taken to build movies recommender systems
- Webscrape image_url and extract url from data in links.csv
- Extract features from movies data (such as genres). 
- Based on the movie genres and users' ratings, 
- Build user profiles dataframe.
- Use the user profile feature vectors and movies genre feature vectors constructed, with several computational methods, such as a simple dot product, to compute or predict an interest score for each movie
- recommend those movies with the highest interest scores.
- Building App Using Streamlit

A user profile can be seen as the user feature vector that mathematically represents a user's learning interests.


### About Dataset

This dataset (ml-latest-small) describes 5-star rating and free-text tagging activity from [MovieLens](http://movielens.org), a movie recommendation service. It contains 100836 ratings and 3683 tag applications across 9742 movies. These data were created by 610 users between March 29, 1996 and September 24, 2018. This dataset was generated on September 26, 2018.

Users were selected at random for inclusion. All selected users had rated at least 20 movies. No demographic information is included. Each user is represented by an id, and no other information is provided.

The data are contained in the files `links.csv`, `movies.csv`, `ratings.csv` and `tags.csv`. More details about the contents and use of all these files follows.

This and other GroupLens data sets are publicly available for download at <http://grouplens.org/datasets/>.# GroupLens-Movies-Recommender

### Website
https://davidsonity-grouplens-movies-recommender-app-m9dj9x.streamlitapp.com/
