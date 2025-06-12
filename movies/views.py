from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.views import View

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = "home.html"
    context_object_name = "movies"



class MovieCreateView(CreateView):
    model = Movie
    template_name = "create_movies.html"
    fields = "__all__"
    success_url = "/"


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
