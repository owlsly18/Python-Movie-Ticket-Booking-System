from services.movie_service import add_movie, remove_movie, list_movies
from services.booking_service import add_showtime, list_all_bookings

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
        elif choice == "0":
            break
        else:
            print("Invalid input. Try again.")
