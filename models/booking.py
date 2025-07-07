class Booking:
    def __init__(self, id, user_name, showtime_id, seat_number, status):
        self.id = id
        self.user_name = user_name
        self.showtime_id = showtime_id
        self.seat_number = seat_number
        self.status = status

    def __str__(self):
        return f"{self.id}. User: {self.user_name} | Showtime ID: {self.showtime_id} | Seat: {self.seat_number} | Status: {self.status}"
