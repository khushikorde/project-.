from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Sample dataset
data = {
    'User': ['A','A','B','B','C','C'],
    'Movie': ['Inception','Titanic','Inception','Avatar','Titanic','Avatar'],
    'Rating': [5,4,4,5,5,4]
}

df = pd.DataFrame(data)
user_movie_matrix = df.pivot_table(index='User', columns='Movie', values='Rating').fillna(0)

# Similarity between movies
similarity = cosine_similarity(user_movie_matrix.T)
similarity_df = pd.DataFrame(similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

def recommend(movie_name):
    print(f"Movies similar to {movie_name}:")
    print(similarity_df[movie_name].sort_values(ascending=False)[1:3])

recommend("Inception")