from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
	movie_title = models.CharField(max_length=100)
	movie_release_date = models.CharField(max_length=20)
	rating = models.FloatField()
	runtime = models.FloatField()
	summary = models.CharField(max_length=500)
	image = models.CharField(max_length=150, default=None)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.movie_title

