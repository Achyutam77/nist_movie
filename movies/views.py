from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Genre, Movie


class MovieListView(ListView):
    model = Movie
    template_name = "home.html"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = Movie.objects.all()
        context["trending_movie"] = Movie.objects.filter(is_trending=True)
        context["genres"] = Genre.objects.all()

        return context


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = "create_movies.html"
    fields = "__all__"
    # exclude = ["category"]
    success_url = "/"
    login_url = "/user/login/"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    context_object_name = "movie"


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "create_movies.html"
    fields = "__all__"
    success_url = "/"


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = "confirm_delete.html"
    success_url = "/"
    context_object_name = "movie"
    login_url = "/user/login/"


# from .forms import MovieForm
# from .models import Movie


# class MovieListView(View):
#     def get(self, request):
#         movies = Movie.objects.all()

#         return render(
#             request,
#             "home.html",
#             {
#                 "movies": movies,
#             },
#         )


# class MovieCreateView(View):
#     def get(self, request):
#         form = MovieForm()
#         return render(request, "create_movies.html", {"form": form})

#     def post(self, request):
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")


# def create_movie(request):
#     form = MovieForm()

#     if request.method == "POST":
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#         else:
#             pass

#     return render(
#         request,
#         "create_movies.html",
#         {"form": form},
#     )
