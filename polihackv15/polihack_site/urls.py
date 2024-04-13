from django.urls import path, include
from . import views

urlpatterns = [
    path    ("", views.home, name="home"),  # Default home URL
    path("home/", views.home, name="home")
]# Default home URL