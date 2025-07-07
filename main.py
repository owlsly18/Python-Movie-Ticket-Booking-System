from utils.db import initialize_db
from services.user_service import user_menu
from services.admin_service import admin_menu

def main():
    initialize_db()

    while True:
        print("\n🎬 Movie Ticket Booking System")
        print("1. User")
        print("2. Admin")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            admin_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
