from django.db import models
from django.urls import reverse
from django.conf import settings

class Genre(models.Model):
    genre_name = models.CharField(max_length=250, null=False, unique=True)
    genre_info = models.CharField(max_length=250, null=False)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.genre_name


GENDER_CHOICES = (
    ('MALE', 'M'),
    ('FEMALE', 'F'),
    ('OTHER', 'O'),
)


class StarCast(models.Model):
    star_name = models.CharField(max_length=250, null=False, unique=True)
    star_bod = models.DateField(max_length=250, null=False, unique=True)
    star_gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=False)
    star_info = models.TextField(null=False)
    image = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='star_images')
    active = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.star_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=250, null=False)
    poster1 = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='movie_posters')
    poster2 = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='movie_posters')
    poster3 = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='movie_posters')
    movie_info = models.TextField(null=False)
    release_date = models.DateField(null=False)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    stars = models.ManyToManyField(StarCast)

    def __str__(self):
        return self.movie_name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class HomeBanner(models.Model):
    banner = models.ImageField(null=False, upload_to='banners')
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.banner.path



