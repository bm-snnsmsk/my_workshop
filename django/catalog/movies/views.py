from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404 ## bir yukarının daha kısa gösterimi için
from .models import Movie

def index(request) :
    movies = Movie.objects.all()
    context = {
        "movies" : movies
    }
    # context = {
    #     "name" :"Sinan şimşek"
    # }
    return render(request, 'movies/list.html', context)

def detail(request, movie_id) :
    ## 1. yöntem
    # try :
    #     movie = Movie.objects.get(pk=movie_id)
    # except Movie.DoesNotExist :
    #     raise Http404("Böyle bir sayfa yok")
    # return render(request, 'movies/detail.html', movie)

    ## 2. yöntem kısa gösterim
    context = {
         "movie" : get_object_or_404(Movie, pk=movie_id) 
    }    
    return render(request, 'movies/detail.html', context)

def search(request) :
    return render(request, 'movies/search.html')