# cinema/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    duration = models.IntegerField()  # Duration in minutes

    def __str__(self):
        return self.title

class Theater(models.Model):
    theater_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.theater_number} - {self.name}"

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    showtime = models.DateTimeField()
    available_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie.title} at {self.theater.name} - {self.showtime}"

class Ticket(models.Model):
    user_name = models.CharField(max_length=255)
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user_name}'s Ticket for {self.screening.movie.title} at {self.screening.theater.name} - {self.screening.showtime}"
