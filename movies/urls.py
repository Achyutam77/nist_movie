from django.urls import path

from .views import MovieCreateView, MovieListView

urlpatterns = [
    path("", MovieListView.as_view(), name="home"),
    path("create-movies", MovieCreateView.as_view(), name="create_movie"),
]
