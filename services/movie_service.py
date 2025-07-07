from utils.db import get_connection
from models.movie import Movie

def list_movies():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No movies available.")
    else:
        print("\n🎥 Available Movies:")
        for row in rows:
            movie = Movie(*row)
            print(movie)

def add_movie():
    title = input("Enter movie title: ")
    genre = input("Enter genre: ")
    duration = input("Enter duration (e.g. 2h 10m): ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies (title, genre, duration) VALUES (?, ?, ?)", (title, genre, duration))
    conn.commit()
    conn.close()
    print(f"✅ Movie '{title}' added successfully.")

def remove_movie():
    list_movies()
    movie_id = input("Enter movie ID to remove: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()
    conn.close()
    print("🗑️ Movie removed.")
