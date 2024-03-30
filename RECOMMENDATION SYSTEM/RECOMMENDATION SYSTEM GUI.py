import tkinter as tk
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
    'Adventure': ['Indiana Jones and the Raiders of the Lost Ark', 'Jurassic Park', 'Pirates of the Caribbean', 'Avatar', 'The Lord of the Rings'],
    'Fantasy': ['Harry Potter and the Sorcerer\'s Stone', 'The Lord of the Rings', 'Pan\'s Labyrinth', 'The Chronicles of Narnia', 'Stardust'],
    'Animation': ['Toy Story', 'Finding Nemo', 'Spirited Away', 'Frozen', 'The Lion King']
}

def recommend_movie(genres):
    selected_movies = [movie for genre in genres for movie in movie_data[genre]]
    return random.choice(selected_movies)

def get_recommendation():
    selected_genres = [genre for genre, var in genre_vars.items() if var.get() == 1]
    if selected_genres:
        recommended_movie = recommend_movie(selected_genres)
        recommendation_text.set(recommended_movie)
    else:
        recommendation_text.set("Please select at least one genre.")

# GUI setup
root = tk.Tk()
root.title("Movie Recommendation System")

genre_vars = {}
for genre in movie_data.keys():
    genre_vars[genre] = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=genre, variable=genre_vars[genre], onvalue=1, offvalue=0)
    checkbox.pack(anchor='w')

button = tk.Button(root, text="Get Recommendation", command=get_recommendation)
button.pack()

recommendation_text = tk.StringVar()
recommendation_label = tk.Label(root, textvariable=recommendation_text)
recommendation_label.pack()

root.mainloop()
