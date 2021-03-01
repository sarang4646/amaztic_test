from django.conf import settings
from rest_framework import serializers
from ..models import Genre, Movie, StarCast


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('genre_name', 'genre_info')


GENDER_CHOICES = (
    ('MALE', 'M'),
    ('FEMALE', 'F'),
    ('OTHER', 'O'),
)


class StarCastSerializer(serializers.ModelSerializer):

    class Meta:
        model = StarCast
        fields = ('star_name', 'star_bod', 'star_gender', 'star_info', 'image')


class MovieSerializer(serializers.ModelSerializer):
    movie_name = serializers.CharField()
    poster1 = serializers.ImageField()
    poster2 = serializers.ImageField()
    poster3 = serializers.ImageField()
    movie_info = serializers.CharField()
    release_date = serializers.DateField()
    genre = GenreSerializer(many=True, read_only=True)
    stars = StarCastSerializer(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = ('movie_name', 'poster1', 'poster2', 'poster3', 'movie_info', 'release_date', 'genre', 'stars')


