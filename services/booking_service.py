from utils.db import get_connection
from models.showtime import Showtime
from models.booking import Booking


def list_showtimes_for_movie(movie_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM showtimes WHERE movie_id = ?", (movie_id,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No showtimes available for this movie.")
        return []

    print("\n🕒 Showtimes:")
    for row in rows:
        show = Showtime(*row)
        print(show)
    return rows

def show_available_seats(showtime_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT total_seats FROM showtimes WHERE id = ?", (showtime_id,))
    result = cursor.fetchone()
    if not result:
        print("Invalid showtime.")
        return

    total_seats = result[0]

    cursor.execute("SELECT seat_number FROM bookings WHERE showtime_id = ? AND status = 'booked'", (showtime_id,))
    booked = [row[0] for row in cursor.fetchall()]

    print("\n🎟️ Available Seats (X = Booked):")
    seats_per_row = 10
    for i in range(1, total_seats + 1):
        if i in booked:
            print("X", end=" ")
        else:
            print(i, end=" ")
        if i % seats_per_row == 0:
            print()
    print()


def book_seat(showtime_id, seat_number, user_name):
    seat_number = int(seat_number)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM showtimes WHERE id = ?", (showtime_id,))
    row = cursor.fetchone()
    if not row:
        print("❌ Invalid showtime.")
        return

    show = Showtime(*row)

    if seat_number < 1 or seat_number > show.total_seats:
        print("❌ Invalid seat number.")
        return

    cursor.execute("""
        SELECT * FROM bookings
        WHERE showtime_id = ? AND seat_number = ? AND status = 'booked'
    """, (showtime_id, seat_number))
    if cursor.fetchone():
        print("❌ Seat already booked.")
        return

    cursor.execute("""
        INSERT INTO bookings (user_name, showtime_id, seat_number, status)
        VALUES (?, ?, ?, 'booked')
    """, (user_name, showtime_id, seat_number))

    cursor.execute("""
        UPDATE showtimes SET available_seats = available_seats - 1
        WHERE id = ?
    """, (showtime_id,))

    conn.commit()
    conn.close()
    print(f"✅ Seat {seat_number} booked for {user_name}!")


def cancel_booking():
    user = input("Enter your name for cancellation: ")
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, showtime_id, seat_number FROM bookings
        WHERE user_name = ? AND status = 'booked'
    """, (user,))
    rows = cursor.fetchall()

    if not rows:
        print("No active bookings found.")
        return

    bookings = [Booking(row[0], user, row[1], row[2], 'booked') for row in rows]

    print("\n📋 Your Bookings:")
    for b in bookings:
        print(b)

    booking_id = input("Enter booking ID to cancel: ")

    cursor.execute("""
        SELECT showtime_id, seat_number FROM bookings WHERE id = ? AND user_name = ?
    """, (booking_id, user))
    booking = cursor.fetchone()

    if not booking:
        print("Invalid booking.")
        return

    showtime_id, seat_number = booking

    cursor.execute("""
        UPDATE bookings SET status = 'cancelled' WHERE id = ?
    """, (booking_id,))
    cursor.execute("""
        UPDATE showtimes SET available_seats = available_seats + 1 WHERE id = ?
    """, (showtime_id,))

    conn.commit()
    conn.close()
    print(f"❌ Booking {booking_id} cancelled.")


def add_showtime():
    from services.movie_service import list_movies
    list_movies()
    movie_id = input("Enter movie ID for the showtime: ")
    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM): ")
    # total_seats = int(input("Enter total seats: "))
    try:
        total_seats = int(input("Enter total seats: "))
    except ValueError:
        print("❌ Enter a valid number.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO showtimes (movie_id, date, time, total_seats, available_seats)
        VALUES (?, ?, ?, ?, ?)
    """, (movie_id, date, time, total_seats, total_seats))

    conn.commit()
    conn.close()
    print("✅ Showtime added.")


def list_all_bookings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.id, b.user_name, m.title, s.date, s.time,
               b.showtime_id, b.seat_number, b.status
        FROM bookings b
        JOIN showtimes s ON b.showtime_id = s.id
        JOIN movies m ON s.movie_id = m.id
    """)
    results = cursor.fetchall()
    conn.close()

    if not results:
        print("No bookings found.")
        return

    print("\n📄 All Bookings:")
    for row in results:
        booking_id = row[0]
        user_name = row[1]
        movie_title = row[2]
        show_date = row[3]
        show_time = row[4]
        showtime_id = row[5]
        seat_number = row[6]
        status = row[7]

        print(f"{booking_id}. User: {user_name} | Movie: {movie_title} | Time: {show_date} {show_time} | Showtime ID: {showtime_id} | Seat: {seat_number} | Status: {status}")

