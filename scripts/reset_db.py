import os
if os.path.exists("data/movies.db"):
    os.remove("data/movies.db")
    print("✅ Database reset.")
else:
    print("No database found to delete.")
