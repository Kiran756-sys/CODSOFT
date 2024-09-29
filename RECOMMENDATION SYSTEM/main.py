# Sample movie dataset with genres
movies = [
    {"title": "Inception", "genres": ["Action", "Sci-Fi", "Drama"]},
    {"title": "The Hangover", "genres": ["Comedy"]},
    {"title": "Titanic", "genres": ["Drama", "Romance"]},
    {"title": "Get Out", "genres": ["Horror", "Thriller"]},
    {"title": "Avengers: Endgame", "genres": ["Action", "Sci-Fi"]},
    {"title": "The Notebook", "genres": ["Drama", "Romance"]},
    {"title": "Joker", "genres": ["Drama", "Thriller"]},
    {"title": "Toy Story", "genres": ["Animation", "Comedy"]},
    {"title": "A Quiet Place", "genres": ["Horror", "Thriller"]},
    {"title": "La La Land", "genres": ["Musical", "Romance"]},
]

# Function to get movie recommendations based on preferred genres
def get_recommendations(preferred_genres):
    recommendations = []

    for movie in movies:
        # Check if any of the movie's genres match the user's preferred genres
        if any(genre in preferred_genres for genre in movie["genres"]):
            recommendations.append(movie["title"])

    return recommendations

# Function to interact with the user and provide recommendations
def recommend_movies():
    print("Welcome to the Movie Recommendation System!")
    print("Here are the available genres:")
    available_genres = set(genre for movie in movies for genre in movie["genres"])
    print(", ".join(available_genres))
    
    # Ask the user for their preferred genres
    user_genres = input("\nEnter your preferred genres (comma-separated): ").split(",")
    user_genres = [genre.strip().capitalize() for genre in user_genres]
    
    # Get movie recommendations based on user preferences
    recommendations = get_recommendations(user_genres)
    
    if recommendations:
        print("\nWe recommend the following movies for you:")
        for movie in recommendations:
            print(f"- {movie}")
    else:
        print("\nSorry, no movies match your preferences.")

# Run the recommendation system
if __name__ == "__main__":
    recommend_movies