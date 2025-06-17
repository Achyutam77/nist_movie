from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    LANGUAGE_CHOICES = [
        ("nepali", "Nepali"),
        ("english", "English"),
        ("hindi", "Hindi"),
    ]
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    release_year = models.IntegerField()
    duration_minutes = models.IntegerField()
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    cover_image_url = models.URLField()
    trailer_url = models.URLField()
    video_url = models.URLField()
    is_trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
