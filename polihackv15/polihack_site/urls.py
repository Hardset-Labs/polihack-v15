from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Default home URL
    path("home/", views.home, name="home"),
    path("subjects/", views.get_subjects, name="subjects"),
    path("study_plan/", views.study_plan, name="study_plan"),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('edit_subject/<int:subject_id>/', views.add_subject, name='edit_subject'),
    path('learn_now/', views.learn_now, name='learn_now'),
    path('learn_subject/<int:subject_id>/', views.learn_subject, name='learn_subject'),
    path('delete_subject/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    path('loading/', views.loading_page, name='loading_page'),
    path('study_plan/', views.study_plan, name='study_plan')
    path('learn_now/<int:last_question_id>/', views.learn_now, name='learn_now'),
    path('loading/', views.loading_page, name='loading_page')
]# Default home URL