from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:id>', category, name='category'),
    path('movie/<int:id>', movie, name='movie'),
    path('star/<int:id>', star, name='star'),

    path('movie_list/', movie_list, name='movie_list'),
    path('star_list/', star_list, name='star_list'),
    path('genre_list/', genre_list, name='genre_list'),

    path('add_movie/', create_movie, name='add_movie'),
    path('add_star/', create_star, name='add_star'),
    path('add_genre/', create_genre, name='add_genre'),

    path('update_movie/<int:id>', update_movie, name='update_movie'),
    path('update_star/<int:id>', update_star, name='update_star'),
    path('update_genre/<int:id>', update_genre, name='update_genre'),

    path('delete_movie/<int:id>', delete_movie, name='delete_movie'),
    path('delete_star/<int:id>', delete_star, name='delete_star'),
    path('delete_genre/<int:id>', delete_genre, name='delete_genre'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)