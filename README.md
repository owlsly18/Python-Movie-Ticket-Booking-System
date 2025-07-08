# 🎬 Movie Ticket Booking System (Python CLI)

A command-line based movie ticket booking system built in Python. This system allows users to browse movies, view showtimes, book or cancel seats, and provides admin controls to manage movies and schedules.

---

## ✨ Features

### 👤 User
- **Browse movies and showtimes**  
- **View available seats**  
- **Book seats**  
- **Cancel bookings**

### 🔧 Admin
- **Secure admin login**
- **Add / Remove movies**
- **Create showtimes with date, time, and total seats**
- **View all bookings with movie and seat details**
- **Seed the database with demo movies**

---

## 🏗️ System Architecture

```plaintext
main.py
│
├── models/
│   ├── booking.py
│   ├── movie.py
│   └── showtime.py
│
├── services/
│   ├── admin_service.py     # Admin dashboard and features
│   ├── booking_service.py   # Handle bookings and showtimes
│   ├── movie_service.py     # Manage movie operations
│   └── user_service.py      # User interaction flow
│
├── scripts/
│   └── reset_db.py          # Script to reset the database
│
├── utils/
│   └── db.py                # Database setup and connection
│
├── data/
│   └── movies.db            # SQLite database (auto-created)
│
└── config.py                # Store constants like admin password
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- Git (optional, for cloning)
- No external dependencies required (standard libraries only)

---

### 📥 Installation

```bash
git clone https://github.com/owlsly18/Python-Movie-Ticket-Booking-System
cd Python-Movie-Ticket-Booking-System
```

Or download and unzip the folder manually.

---

### ▶️ Running the App

```bash
python main.py
```

---

### 🔐 Admin Access

To access the admin menu, use the following:

```text
Password: admin123
```

(You can change this in `config.py`)

---

## 📋 Sample Usage Flow

### 👤 User Flow

1. Choose **User** from main menu  
2. Select a movie → view showtimes  
3. Select showtime → view available seats  
4. Choose seat → enter name → confirm booking  
5. Optionally cancel any booking by its ID  

---

### 🔧 Admin Flow

1. Choose **Admin** → enter password  
2. Add movies or use **Option 5: Add Demo Movies**  
3. Add showtimes (specifying date, time, seat count)  
4. View all user bookings with movie & seat info  

---

## 🧪 Resetting the Database

### ✅ Option 1: Use Reset Script (Recommended)

```bash
python scripts/reset_db.py
```

This will:
- Delete the existing `movies.db` file
- Recreate all required tables
- You can then login as Admin and:
  - Add movies manually
  - Or use Option 5: Add Demo Movies

---

### 🛠 Option 2: Manual Reset (Not recommended)

```bash
rm data/movies.db
python main.py
```

This will recreate the database automatically.

---

## 📦 Directory Structure

```plaintext
.
├── main.py
├── config.py
├── data/
├── models/
├── services/
├── scripts/
├── utils/
├── .gitignore
└── README.md
```

---

## ✅ Built With

- Python 3.8+
- SQLite (sqlite3)
- Pure Python CLI (No GUI or web framework)

---

## 🧠 AI & Tools Used

- **ChatGPT (OpenAI)** — for development assistance
- **Git & GitHub** — for version control and sharing

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙋‍♂️ Author

**Dushyant Ranjit**  
📧 [dushyant.ranjit@gmail.com](mailto:dushyant.ranjit@gmail.com)  
🌐 [dushyantranjit.com.np](https://dushyantranjit.com.np)  
🐙 [github.com/owlsly18](https://github.com/owlsly18)
