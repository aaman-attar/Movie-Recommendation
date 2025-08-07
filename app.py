from flask import Flask, render_template, request
import pandas as pd
from recommendation import get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre']
    recommendations = get_recommendations_by_genre(genre)
    return render_template('recommend.html', recommendations=recommendations.to_dict(orient='records'))

def get_recommendations_by_genre(genre):
    df = pd.read_csv('cleaned_movies.csv')
    genre_movies = df[df['genres'].str.contains(genre, case=False, na=False)]
    
    all_recs = []
    for title in genre_movies['title'].head(5):  # Recommend for top 5 in genre
        recs = get_recommendations(title)
        all_recs.extend(recs.to_dict(orient='records'))
    
    recommendations_df = pd.DataFrame(all_recs).drop_duplicates(subset='title')
    return recommendations_df.sort_values(by='rating', ascending=False)

if __name__ == '__main__':
    app.run(debug=True)
