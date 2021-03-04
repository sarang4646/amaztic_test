from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Genre, Movie, HomeBanner, StarCast
from .forms import GenreUpdateForm, GenreCreateForm, StarCastUpdateForm, StarCastCreateForm, MovieUpdateForm, MovieCreateForm


def index(request):
    page_title = 'movieapp : home'
    genres = Genre.objects.filter(active=True)
    genres_head = Genre.objects.filter(active=True)[:5]
    home_banners = HomeBanner.objects.filter(active=True)
    movies = Movie.objects.filter(active=True)
    context = {
        'page_title': page_title,
        'genres_head': genres_head,
        'genres': genres,
        'home_banners': home_banners,
        'movies': movies,
    }
    return render(request, 'backend/index.html', context)


def category(request, id):
    page_title = 'movieapp : home'
    genres = Genre.objects.get(id=id)
    genres_head = Genre.objects.filter(active=True)[:5]
    movies = Movie.objects.filter(active=True)
    context = {
        'page_title': page_title,
        'genres_head': genres_head,
        'genres': genres,
        'movies': movies,
    }
    return render(request, 'backend/category.html', context)


def movie(request, id):
    page_title = 'movieapp : home'
    genres = Genre.objects.filter(active=True)
    genres_head = Genre.objects.filter(active=True)[:5]
    movies = Movie.objects.filter(id=id)
    context = {
        'page_title': page_title,
        'genres_head': genres_head,
        'genres': genres,
        'movies': movies,
        'movie': movie,
        # 'rel_ms': rel_ms
    }
    return render(request, 'backend/movie.html', context)


def star(request, id):
    page_title = 'movieapp : home'
    genres = Genre.objects.filter(active=True)
    genres_head = Genre.objects.filter(active=True)[:5]
    stars = StarCast.objects.filter(id=id)
    movies = Movie.objects.filter(stars__id=id)

    context = {
        'page_title': page_title,
        'genres_head': genres_head,
        'genres': genres,
        'stars': stars,
        'movies': movies,
    }
    return render(request, 'backend/star.html', context)


@login_required
def movie_list(request):
    if request.method == 'POST':
        return redirect('movie_list')
    else:
        context = {
            'movies': Movie.objects.filter(author=request.user)
        }
        pass
    return render(request, 'backend/movie_list.html', context)


@login_required
def create_movie(request):
    if request.method == 'POST':
        movie = Movie()
        form = MovieCreateForm(request.POST, request.FILES, instance=movie)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, f'Data Created!')
            return redirect('movie_list')
    else:
        movie = Movie()
        form = MovieCreateForm(instance=movie)
    context = {
        'form': form,
    }
    return render(request, 'backend/create_movie_1.html', context)


@login_required
def update_movie(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        form = MovieUpdateForm(request.POST, request.FILES, instance=movie)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, f'Data updated!')
            return redirect('movie_list')
    else:
        movie = Movie.objects.get(id=id)
        form = MovieUpdateForm(instance=movie)
    context = {
        'form': form,
    }
    return render(request, 'backend/create_movie_1.html', context)


@login_required
def delete_movie(request, id):
    Movie.objects.get(id=id).delete()
    messages.success(request, f'Data Deleted!')
    return redirect('movie_list')


@login_required
def star_list(request):
    if request.method == 'POST':
        return redirect('star_list')
    else:
        context = {
            'starCast': StarCast.objects.filter(author=request.user)
        }
        pass
    return render(request, 'backend/star_list.html', context)


@login_required
def create_star(request, id=None):
    if request.method == 'POST':
        star = StarCast()
        form = StarCastCreateForm(request.POST, request.FILES, instance=star)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, f'Data Created!')
            return redirect('star_list')
    else:
        star = StarCast()
        form = StarCastCreateForm(instance=star)
    context = {
        'form': form,
    }
    return render(request, 'backend/create_star.html', context)


@login_required
def update_star(request, id):
    if request.method == 'POST':
        star = StarCast.objects.get(id=id)
        form = StarCastUpdateForm(request.POST, request.FILES, instance=star)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, f'Data updated!')
            return redirect('star_list')
    else:
        star = StarCast.objects.get(id=id)
        form = StarCastUpdateForm(instance=star)
    context = {
        'form': form,
    }
    return render(request, 'backend/create_star.html', context)


@login_required
def delete_star(request, id):
    StarCast.objects.get(id=id).delete()
    messages.success(request, f'Data Deleted!')
    return redirect('star_list')


@login_required
def genre_list(request):
    if request.method == 'POST':
        return redirect('genre_list')
    else:
        context = {
            'genres': Genre.objects.filter(author=request.user)
        }
        pass
    return render(request, 'backend/genre_list.html', context)


@login_required
def create_genre(request):
    if request.method == 'POST':
        genre = genre = Genre()
        form = GenreCreateForm(request.POST, instance=genre)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, f'Data Created!')
            return redirect('genre_list')
    else:
        genre = Genre()
        form = GenreCreateForm(instance=genre)
    context = {
        'form': form,
    }
    return render(request, 'backend/create_genre.html', context)


@login_required
def update_genre(request, id):
    if request.method == 'POST':
        genre = Genre.objects.get(id=id)
        form = GenreUpdateForm(request.POST, instance=genre)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, f'Data updated!')
            return redirect('genre_list')
    else:
        genre = Genre.objects.get(id=id)
        form = GenreUpdateForm(instance=genre)
    context = {
        'form': form,
    }
    return render(request, 'backend/create_genre.html', context)


@login_required
def delete_genre(request, id):
    Genre.objects.get(id=id).delete()
    messages.success(request, f'Data Deleted!')
    return redirect('genre_list')
