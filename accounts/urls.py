from django.urls import path
from .views import dashboard,registration,AddMovie,FavMovies

urlpatterns = [
    path('sign-up',registration,name='signup'),
    path('',dashboard,name='dashboard'),
    path('add-movie',AddMovie.as_view(),name='add_movie'),
    path('movies',FavMovies.as_view(),name='list_movies')
]
