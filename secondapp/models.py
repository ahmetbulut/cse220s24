from django.db import models

# Create your models here.
class Dummy(models.Model):
    name = models.CharField(max_length=100)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' at ' + self.email

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.name + ' released on ' + str(self.release_date)

class Rating(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return self.customer.name + ' rated ' + self.movie.name + ' with ' + str(self.rating) + ' stars'