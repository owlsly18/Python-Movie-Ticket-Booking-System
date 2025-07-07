from services.movie_service import list_movies
from services.booking_service import list_showtimes_for_movie, show_available_seats, book_seat, cancel_booking

def user_menu():
    while True:
        print("\n👤 User Menu")
        print("1. Browse Movies")
        print("2. Cancel Booking")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            list_movies()
            movie_id = input("Enter Movie ID to view showtimes (or 0 to go back): ")
            if movie_id == "0": continue

            list_showtimes_for_movie(movie_id)
            showtime_id = input("Enter Showtime ID to see available seats: ")

            show_available_seats(showtime_id)
            seat = input("Enter seat number to book (or 0 to cancel): ")
            if seat == "0": continue
            name = input("Enter your name: ")
            book_seat(showtime_id, seat, name)

        elif choice == "2":
            cancel_booking()

        elif choice == "0":
            break
        else:
            print("Invalid input. Try again.")
