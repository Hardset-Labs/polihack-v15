from django.http import JsonResponse
from django.shortcuts import render
from .models import UserData

# Create your views here.
def home(request):
    return render(request, 'polihack_site/home.html')


def add_subject(request):
    return render(request, 'polihack_site/add_subject.html')


def create_learning_plan(request):
    return JsonResponse({'status': 'success'})


def get_user_data(request):
    # Create a new user (you can customize this as needed)
    
    # Create a new UserData object with hardcoded values
    user_data = UserData(user="Mirel", lives=3, streak=0)
    
    # Pass the user_data to the template
    return render(request, 'polihack_site/base.html', {'user_data': user_data})

