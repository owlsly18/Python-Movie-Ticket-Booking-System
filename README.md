🚀 Getting Started
🔧 Prerequisites
Python 3.8+

Git (optional, for cloning)

💡 No external dependencies required — everything is built with standard libraries.

📥 Installation
bash
Copy
Edit
git clone https://github.com/owlsly18/Python-Movie-Ticket-Booking-System
cd Python-Movie-Ticket-Booking-System
Or download and unzip the folder manually.

▶️ Running the App
bash
Copy
Edit
python main.py
🔐 Admin Access
Password: admin123

(Stored in config.py — can be changed if needed)

🧪 Resetting the Database
✅ Option 1: Use Reset Script (Recommended)
bash
Copy
Edit
python scripts/reset_db.py
This will:

Delete the existing movies.db file

Recreate all necessary tables

You can then login as Admin and:

Add movies manually

Or use option 5. Add Demo Movies

🛠 Option 2: Manual Reset (Not recommended)
bash
Copy
Edit
rm data/movies.db
python main.py
📋 Sample Usage Flow
👤 User Flow:
Choose User from main menu

Select a movie → view showtimes

Select showtime → view available seats

Choose seat → enter name → confirm booking

Optionally cancel bookings by ID

🔧 Admin Flow:
Choose Admin → enter password

Add movies or use Add Demo Movies

Create showtimes

View all bookings

✅ Built With
Python 3.8+

SQLite (sqlite3)

Pure Python CLI

🧠 AI & Tools Used
ChatGPT (OpenAI): for development assistance

Git & GitHub: version control and sharing

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Dushyant Ranjit
📧 dushyant.ranjit@gmail.com
🌐 dushyantranjit.com.np
🐙 github.com/owlsly18