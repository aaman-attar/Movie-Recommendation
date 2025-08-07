# 🎬 Movie Recommendation System

This is a simple web-based **Movie Recommendation System** built using Python, Streamlit, and HTML. It recommends movies similar to the user’s selected genre using content-based filtering.

---

## 📂 Project Structure

The project contains the following key files:

### 🚀 Main Application Files

| File                    | Description                                                  |
|-------------------------|--------------------------------------------------------------|
| `app.py`                | Main Python script that runs the Streamlit web app.          |
| `recommendation.py`     | Logic to generate movie recommendations using cosine similarity. |
| `templates/index.html`  | Landing page of the web interface (genre selection).         |
| `templates/recommend.html` | Page to display recommended movies and chart.             |
| `cleaned_movies.csv`    | Final dataset used to generate recommendations.              |

### 📊 Dataset Preparation Files (used to create `cleaned_movies.csv`)

| File               | Description                                            |
|--------------------|--------------------------------------------------------|
| `merged.csv`       | Raw movie metadata file.                               |
| `ratings.csv`      | User ratings dataset.                                  |
| `merged_data.csv`  | Intermediate dataset after merging movies and ratings. |
| `data_preparation.csv` | Script to preprocess and generate cleaned data.    |

---

## 🔧 Setup Instructions

Follow these steps to run the project locally:

1. Clone the Repository
bash:
git clone https://github.com/your-username/movie-recommendation.git
cd movie-recommendation

2. Create a Virtual Environment
python -m venv venv

3. Activate the Virtual Environment
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

4. Install the Requirements
Make sure a requirements.txt file is present, then run:
pip install -r requirements.txt

5. Run the App
streamlit run app.py
