from django.db import models

# Create your models here.
class Barangmywatchlist(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.TextField()
    release_date = models.TextField()
    review = models.TextField()