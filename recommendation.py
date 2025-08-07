# recommendation.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load preprocessed movie data
movies_df = pd.read_csv('cleaned_movies.csv')  # ✅ Ensure this file has 'title' and 'genres'

# Combine important features for similarity
movies_df['combined'] = movies_df['title'].fillna('') + ' ' + movies_df['genres'].fillna('')

# Vectorize the combined column
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies_df['combined'])

# Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Map movie titles to index
indices = pd.Series(movies_df.index, index=movies_df['title'].str.lower()).drop_duplicates()

def get_recommendations(title, top_n=10):
    title = title.lower()
    
    if title not in indices:
        return pd.DataFrame(columns=['title', 'rating'])

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    movie_indices = [i[0] for i in sim_scores]
    recommended = movies_df.iloc[movie_indices][['title']]
    recommended['rating'] = 4.0  # Optional: add dummy rating if not merging with ratings.csv

    return recommended
