from services.movie_service import add_movie, remove_movie, list_movies
from services.booking_service import add_showtime, list_all_bookings
from utils.db import get_connection

def seed_demo_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies (title, genre, duration) VALUES ('Inception', 'Sci-Fi', '2h 28m')")
    cursor.execute("INSERT INTO movies (title, genre, duration) VALUES ('Interstellar', 'Sci-Fi', '2h 49m')")
    conn.commit()
    conn.close()
    print("🎉 Demo movies added.")

def admin_menu():
    password = input("Enter admin password: ")
    if password != "admin123":
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
