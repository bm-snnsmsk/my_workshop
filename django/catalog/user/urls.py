from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"), ## http://127.0.0.8000/user/login
    path("register/", views.register, name="register"), ## http://127.0.0.8000/user/register
    path("logout/", views.logout, name="logout"), ## http://127.0.0.8000/user/logout
]