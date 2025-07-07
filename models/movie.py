class Movie:
    def __init__(self, id, title, genre, duration):
        self.id = id
        self.title = title
        self.genre = genre
        self.duration = duration

    def __str__(self):
        return f"{self.id}. {self.title} | Genre: {self.genre} | Duration: {self.duration}"
