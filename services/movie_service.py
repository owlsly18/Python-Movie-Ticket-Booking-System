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
        return []

    print("\n🎥 Available Movies:")
    for row in rows:
        movie = Movie(*row)
        print(movie)
    return rows

def add_movie():
    title = input("Enter movie title: ").strip()
    genre = input("Enter genre: ").strip()
    duration = input("Enter duration (e.g. 2h 30m): ").strip()

    if not title or not genre or not duration:
        print("❌ All fields are required.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    # Check if the movie already exists by title
    cursor.execute("SELECT id FROM movies WHERE LOWER(title) = LOWER(?)", (title,))
    if cursor.fetchone():
        print("⚠️ Movie already exists.")
        conn.close()
        return

    cursor.execute(
        "INSERT INTO movies (title, genre, duration) VALUES (?, ?, ?)",
        (title, genre, duration)
    )
    conn.commit()
    conn.close()
    print("✅ Movie added successfully.")

def remove_movie():
    list_movies()
    movie_id = input("Enter movie ID to remove: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()
    conn.close()
    print("🗑️ Movie removed.")
