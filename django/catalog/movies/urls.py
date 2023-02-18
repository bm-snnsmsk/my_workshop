from django.urls import path
from . import views


## http://127.0.0.8000/movies   
urlpatterns = [
    path("", views.index, name="movies"), ## http://127.0.0.8000/movies
    path("<int:movie_id>", views.detail, name="detail"), ## http://127.0.0.8000/movies/2    = 2 örnek
    path("search", views.search, name="search") ## http://127.0.0.8000/movies/search
]