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


def subjects(request):
    return render(request, 'polihack_site/subjects.html')


def get_user_data(request):
    # Create a new user (you can customize this as needed)
    
    # Create a new UserData object with hardcoded values
    user_data = UserData(user="Mirel", lives=3, streak=0)
    
    # Pass the user_data to the template
    return render(request, 'polihack_site/base.html', {'user_data': user_data})


def learn(request):
    # Sample question object
    question = {
        'question': 'What is the capital of France?',
        'dummy_answer1': 'Berlin',
        'dummy_answer2': 'London',
        'dummy_answer3': 'Budapest',
        'correct_answer': 'Paris',
        'explanation': 'The capital of France is Paris.'
    }

    context = {
        'question': question,
    }

    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        is_correct = selected_answer == question['correct_answer']
        response_data = {
            'is_correct': is_correct,
            'explanation': question['explanation']
        }
        return JsonResponse(response_data)

    context = {
        'question': question,
    }
    return render(request, 'polihack_site/learn.html', context)