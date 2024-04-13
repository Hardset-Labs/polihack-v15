from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Default home URL
    path("home/", views.home, name="home"),
    path("subjects/", views.subjects, name="subjects"),
    path("study_plan/", views.study_plan, name="study_plan"),
]# Default home URL