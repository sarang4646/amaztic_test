from django import forms
from core.backend.models import *


class GenreUpdateForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_name', 'genre_info']


class GenreCreateForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_name', 'genre_info']


class StarCastUpdateForm(forms.ModelForm):
    star_bod = forms.DateField()

    class Meta:
        model = StarCast
        fields = ['star_name', 'star_bod', 'star_gender', 'star_info', 'image']


class StarCastCreateForm(forms.ModelForm):
    star_bod = forms.DateField()

    class Meta:
        model = StarCast
        fields = ['star_name', 'star_bod', 'star_gender', 'star_info', 'image']


class MovieUpdateForm(forms.ModelForm):
    release_date = forms.DateField()
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())
    stars = forms.ModelMultipleChoiceField(queryset=StarCast.objects.all())

    class Meta:
        model = Movie
        fields = ['movie_name', 'poster1', 'poster2', 'poster3', 'movie_info', 'release_date', 'genre', 'stars']


class MovieCreateForm(forms.ModelForm):
    release_date = forms.DateField()
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())
    stars = forms.ModelMultipleChoiceField(queryset=StarCast.objects.all())

    class Meta:
        model = Movie
        fields = ['movie_name', 'poster1', 'poster2', 'poster3', 'movie_info', 'release_date', 'genre', 'stars']