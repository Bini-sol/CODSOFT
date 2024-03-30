import random

# Define movie genres and titles
movie_data = {
    'Action': ['Die Hard', 'The Dark Knight', 'Inception', 'Mad Max: Fury Road', 'The Matrix'],
    'Comedy': ['Superbad', 'The Hangover', 'Anchorman', 'Dumb and Dumber', 'Bridesmaids'],
    'Drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather', 'Schindler\'s List', 'Pulp Fiction'],
    'Thriller': ['Seven', 'Gone Girl', 'Shutter Island', 'The Silence of the Lambs', 'The Sixth Sense'],
    'Sci-Fi': ['Interstellar', 'Blade Runner', 'Avatar', 'Alien', 'The Martian'],
    'Horror': ['The Shining', 'Halloween', 'A Nightmare on Elm Street', 'The Exorcist', 'Get Out'],
    'Romance': ['Titanic', 'The Notebook', 'La La Land', 'Pride and Prejudice', 'Before Sunrise'],
    'Adventure': ['Indiana Jones and the Raiders of the Lost Ark', 'Jurassic Park', 'Pirates of the Caribbean',
                  'Avatar', 'The Lord of the Rings'],
    'Fantasy': ['Harry Potter and the Sorcerer\'s Stone', 'The Lord of the Rings', 'Pan\'s Labyrinth',
                'The Chronicles of Narnia', 'Stardust'],
    'Animation': ['Toy Story', 'Finding Nemo', 'Spirited Away', 'Frozen', 'The Lion King']
}


def recommend_movie(genres):
    selected_movies = [movie for genre in genres for movie in movie_data[genre]]
    return random.choice(selected_movies)


def get_recommendation(selected_genres):
    if selected_genres:
        recommended_movie = recommend_movie(selected_genres)
        return recommended_movie
    else:
        return "Please select at least one genre."


def main():
    print("Welcome to the Movie Recommendation System!")
    print("Available genres:")
    for genre in movie_data.keys():
        print(f"- {genre}")

    selected_genres = input("Enter genres you like (comma-separated): ").split(',')
    selected_genres = [genre.strip() for genre in selected_genres]

    recommendation = get_recommendation(selected_genres)
    print("Recommended movie:", recommendation)


if __name__ == "__main__":
    main()

