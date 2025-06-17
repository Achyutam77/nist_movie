
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer

not_found_message = {"detail":"Movie Not Found"}

@api_view(["GET", "POST"])
def movie_list_view(request):
    if request.method == "POST":
        movie = MovieSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response(
                {
                    "result": "Movie created successfully",
                },
            )
        else:
            pass


    movies_objects = Movie.objects.all()
    movie = MovieSerializer(movies_objects, many=True)

    return Response(movie.data)

@api_view(["GET","PUT","DELETE"])
def movie_detail_view(request, pk):
    if request.method == "GET":
        try:
            movie_obj = Movie.objects.get(pk=pk)
            movie = MovieSerializer(movie_obj)
            return Response(movie.data)
        except Movie.DoesNotExist:
            return Response(not_found_message)

    if request.method == "PUT":
        try:
            movie_obj = Movie.objects.get(pk=pk)
            updated_movie = MovieSerializer(movie_obj,request.data)
            if updated_movie.is_valid():
                updated_movie.save()
                return Response(updated_movie.data)
            else:
                return Response(updated_movie.errors)
        except Movie.DoesNotExist:
            return Response(not_found_message)

    if request.method == "DELETE":
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
        except Movie.DoesNotExist:
            return Response(not_found_message)

        
        

