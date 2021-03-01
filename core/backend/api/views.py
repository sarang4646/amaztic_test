from .serializers import GenreSerializer, StarCastSerializer, MovieSerializer
from ..models import Genre, Movie, StarCast
from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin



class MovieList(ListAPIView, ListModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
