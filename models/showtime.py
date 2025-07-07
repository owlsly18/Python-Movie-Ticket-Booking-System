class Showtime:
    def __init__(self, id, movie_id, date, time, total_seats, available_seats):
        self.id = id
        self.movie_id = movie_id
        self.date = date
        self.time = time
        self.total_seats = total_seats
        self.available_seats = available_seats

    def __str__(self):
        return f"{self.id}. Date: {self.date}, Time: {self.time}, Seats Left: {self.available_seats}"
