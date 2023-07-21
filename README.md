## **MovieLens Recommender+**
> A Collaborative Filtering Based Recommender System 

<center>
    <img src= "https://res.cloudinary.com/practicaldev/image/fetch/s--hGvhAGUu--/c_imagga_scale,f_auto,fl_progressive,h_500,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/mih10uhu1464fx1kr0by.jpg" width="800" alt="cognitiveclass.ai logo" />
</center>

### Introduction
This project aims to build a movie recommender system using collaborative filtering based on the MovieLens dataset. Collaborative filtering is a popular technique used in recommendation systems to suggest items to users based on the preferences and behavior of similar users. In this case, we focus on user-based collaborative filtering, where the similarity between users is used to make movie recommendations.

### Objective
The main objective of this project is to develop a movie recommender system that suggests movies to users based on their past movie ratings and the ratings of similar users.

### Dataset
The dataset used in this project is the MovieLens dataset, which includes 100,836 ratings and 3,683 tag applications across 9,742 movies. The data was created by 610 users between March 29, 1996, and September 24, 2018. The dataset contains no demographic information, and each user is represented by an ID. The data files used are links.csv, movies.csv, ratings.csv, and tags.csv.

### Methodology
1. **Data Loading and Preprocessing:** The project starts by loading the movies and ratings dataframes from CSV files. We also create a user-item interaction matrix that represents the ratings given by users to different movies.

2. **Collaborative Filtering Algorithms:** Two collaborative filtering algorithms are employed for recommendation:
   - Singular Value Decomposition (SVD): This algorithm factorizes the user-item interaction matrix to find latent features and make predictions.
   - k-Nearest Neighbors (k-NN): This algorithm computes the similarity between users based on their ratings and recommends items based on similar users' preferences.

3. **Training and Evaluation:** The algorithms are trained on the dataset using the Surprise library. The evaluation is done using Root Mean Squared Error (RMSE) as a metric to measure the performance of the models.

4. **Model Saving:** The trained k-NN model is saved to a file using the Python pickle module for future use.

5. **Web Scraping for Image URLs:** Image URLs for movie posters are scraped from the web using BeautifulSoup. These URLs are then saved to a CSV file.

6. **Making Recommendations:** For a specific user, the saved k-NN model is used to generate the top-10 movie recommendations based on their past ratings and the ratings of similar users.

### Results
The collaborative filtering algorithms are evaluated using RMSE, and the k-NN algorithm outperformed SVD with an RMSE of 0.94225.

### Deployment Site
Visit the deployment site to experience the Movie Recommender System:
[Movie Recommender System](https://davidsonity-grouplens-movies-recommender-app-m9dj9x.streamlitapp.com/)

### Project Structure
The repository contains the following files:
- data/: Folder containing the MovieLens dataset CSV files.
- notebook.ipynb: Jupyter notebook containing the code for data preprocessing, model training, and evaluation.
- knn_model.pkl: Pickle file containing the saved k-NN model.
- link_df.csv: CSV file with scraped image URLs.
- README.md: Detailed project description and instructions.

### Instructions to Run
1. Clone the repository to your local machine.
2. Install the required libraries mentioned in the notebook.
3. Run the Jupyter notebook 'notebook.ipynb' to train the collaborative filtering models and save the k-NN model.
4. You can use the saved k-NN model for making movie recommendations for specific users.
5. The image URLs scraped from the web are available in 'link_df.csv' for further use.