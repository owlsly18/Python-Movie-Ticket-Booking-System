import sqlite3

def get_connection():
    return sqlite3.connect("data/movies.db")

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT,
            duration TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS showtimes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER,
            date TEXT,
            time TEXT,
            total_seats INTEGER,
            available_seats INTEGER,
            FOREIGN KEY(movie_id) REFERENCES movies(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            showtime_id INTEGER,
            seat_number INTEGER,
            status TEXT,
            FOREIGN KEY(showtime_id) REFERENCES showtimes(id)
        )
    ''')

    conn.commit()
    conn.close()
