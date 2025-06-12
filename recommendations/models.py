from django.contrib.auth.models import User
from django.db import models

from movies.models import Movie


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.FloatField()
    recommended_at = models.DateTimeField(auto_now=True)
