from .models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        #exclude = ['id', 'created_at', 'updated_at'] #exclude specific fields if needed