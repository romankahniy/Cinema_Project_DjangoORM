from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return f"А '{self.name}' for {self.rows * self.seats_in_row} people"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)


class MovieSession(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} screening in the {self.cinema_hall.name} at {self.show_time}"


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    movie_session = models.ForeignKey(MovieSession, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie_session.movie.title} ticket date: {self.order.created_at} \n " \
               f"{self.row} row {self.seat} place"
