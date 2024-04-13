from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Default home URL
    path("home/", views.home, name="home"),
    path("subjects/", views.subjects, name="subjects"),
    path('add_subject/', views.add_subject, name='add_subject')
]# Default home URL