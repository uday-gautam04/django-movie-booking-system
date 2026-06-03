from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.IntegerField()
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_time = models.TimeField()

    def __str__(self):
        return f"{self.movie.title} - {self.show_time}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.IntegerField()
    name = models.CharField(max_length=100)

    # ✅ FIX ADDED HERE
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.booking_date}"