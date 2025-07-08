from services.movie_service import add_movie, remove_movie, list_movies
from services.booking_service import add_showtime, list_all_bookings
from utils.db import get_connection
from config import ADMIN_PASSWORD


def seed_demo_data():
    demo_movies = [
        ("Inception", "Sci-Fi", "2h 28m"),
        ("Interstellar", "Sci-Fi", "2h 49m"),
        ("The Dark Knight", "Action", "2h 32m")
    ]

    conn = get_connection()
    cursor = conn.cursor()

    added = 0
    for title, genre, duration in demo_movies:
        cursor.execute("SELECT id FROM movies WHERE LOWER(title) = LOWER(?)", (title.lower(),))
        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO movies (title, genre, duration) VALUES (?, ?, ?)",
                (title, genre, duration)
            )
            added += 1

    conn.commit()
    conn.close()

    if added:
        print(f"🎉 {added} demo movie(s) added.")
    else:
        print("✅ Demo movies already exist. No new movies added.")


def admin_menu():
    password = input("Enter admin password: ")
    if password != ADMIN_PASSWORD:
        print("Access Denied.")
        return

    while True:
        print("\n🔧 Admin Menu")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. Add Showtime")
        print("4. View All Bookings")
        print("5. Add Demo Movies")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            remove_movie()
        elif choice == "3":
            add_showtime()
        elif choice == "4":
            list_all_bookings()
        elif choice == "5":
            seed_demo_data()
        elif choice == "0":
            break
        else:
            print("Invalid input. Try again.")
