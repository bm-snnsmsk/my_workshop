from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), ## http://127.0.0.8000
    path("about", views.about, name="about") ## http://127.0.0.8000/about
]