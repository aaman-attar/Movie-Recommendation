import pandas as pd

# Load datasets
movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')

# Display the first few rows of each dataset
print("Movies Data:")
print(movies_df.head())

print("\nRatings Data:")
print(ratings_df.head())

# Check for missing values
print("\nMissing Values:")
print(movies_df.isnull().sum())
print(ratings_df.isnull().sum())

# Drop rows with missing values if necessary
movies_df.dropna(inplace=True)
ratings_df.dropna(inplace=True)

# Ensure genres are strings and concatenate them with spaces
movies_df['genres'] = movies_df['genres'].apply(lambda x: ' '.join(x.split('|')))

# Save the cleaned movies data if needed
movies_df.to_csv('cleaned_movies.csv', index=False)

# Merge datasets on movieId
merged_df = pd.merge(ratings_df, movies_df[['movieId', 'title', 'genres']], on='movieId')

# Save the merged dataframe if needed
merged_df.to_csv('merged_data.csv', index=False)

print("Cleaned Movies Data:")
print(movies_df.head())

print("\nMerged Data:")
print(merged_df.head())
