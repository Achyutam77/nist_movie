from django.urls import path
from .api_view import movie_list_view, movie_detail_view

from .views import (
    MovieCreateView,
    MovieDeleteView,
    MovieDetailView,
    MovieListView,
    MovieUpdateView,
)

urlpatterns = [
    path("api/movies/", movie_list_view),
    path("api/movies/<int:pk>",movie_detail_view),

    path("", MovieListView.as_view(), name="home"),
    path("create-movies", MovieCreateView.as_view(), name="create_movie"),
    path("<int:pk>", MovieDetailView.as_view(), name="movie_detail"),
    path("update_movie/<int:pk>", MovieUpdateView.as_view(), name="movie_update"),
    path("delete_movie/<int:pk>", MovieDeleteView.as_view(), name="movie_delete"),
]
