from django.contrib import admin

from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "genre", "release_year", "language", "duration_minutes"]
    list_filter = ["genre", "language", "release_year"]
    search_fields = ["title", "description"]


admin.site.register(Movie, MovieAdmin)
