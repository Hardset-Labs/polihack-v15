from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Default home URL
    path("home/", views.home, name="home"),
    path("subjects/", views.get_subjects, name="subjects"),
    path("study_plan/", views.study_plan, name="study_plan"),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('edit_subject/<int:item_id>/', views.edit_subject, name='edit_subject')
]# Default home URL