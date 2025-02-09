import pandas as pd
import numpy as np

data = {
    "Movie Name": ["Inception", "3 Idiots", "Parasite", "Interstellar", "Dangal", "The Dark Knight", "PK", "Joker", "Lagaan", "The Godfather"],
    "Language": ["English", "Hindi", "Korean", "English", "Hindi", "English", "Hindi", "English", "Hindi", "English"],
    "Genre": ["Sci-Fi", "Comedy", "Thriller", "Sci-Fi", "Drama", "Action", "Comedy", "Crime", "Sports", "Crime"],
    "Rating": [8.8, 8.4, 8.6, 8.6, 8.4, 9.0, 8.1, 8.4, 8.1, 9.2],
    "Review": [
        "Mind-bending thriller", "Inspirational and funny", "Masterpiece of storytelling", "Visually stunning",
        "Heartwarming sports drama", "Brilliantly dark and intense", "Thought-provoking", "Dark and powerful",
        "Epic historical drama", "Timeless classic"
    ]
}

df = pd.DataFrame(data)
df.to_csv("Movies.csv", index=False)

df = pd.read_csv("Movies.csv")

highest_rated_movie = df.loc[df['Rating'].idxmax()]
print("Movie with highest rating:\n", highest_rated_movie)

hindi_movies = df[df["Language"] == "Hindi"]
hindi_movies.to_csv("HindiMovies.csv", index=False)
print("Hindi movies written to HindiMovies.csv")
