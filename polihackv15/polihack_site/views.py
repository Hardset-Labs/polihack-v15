from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'polihack_site/home.html')


def add_subject(request):
    return render(request, 'polihack_site/add_subject.html')


def create_learning_plan(request):
    return JsonResponse({'status': 'success'})
