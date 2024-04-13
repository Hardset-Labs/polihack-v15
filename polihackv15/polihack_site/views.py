from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import SubjectForm, LearningMinutesDayForm
from .models import UserData, Subject, LearningMinutesDay


LearningMinutesDayFormSet = formset_factory(LearningMinutesDayForm, extra=1)


# Create your views here.
def home(request):
    return render(request, 'polihack_site/home.html')


def add_subject(request):
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST, request.FILES)
        minutes_formset = LearningMinutesDayFormSet(request.POST)

        if subject_form.is_valid() and minutes_formset.is_valid():
            subject = subject_form.save(commit=False)
            subject.user = request.user  # Assuming you have a user associated with the subject
            subject.save()

            for form in minutes_formset:
                if form.cleaned_data:
                    date = form.cleaned_data['date']
                    minutes = form.cleaned_data['minutes']
                    LearningMinutesDay.objects.create(subject=subject, date=date, minutes=minutes)

            return redirect('polihack_site/add_subject')  # Use the correct namespace and URL name

    else:
        subject_form = SubjectForm()
        minutes_formset = LearningMinutesDayFormSet()

    context = {
        'subject_form': subject_form,
        'minutes_formset': minutes_formset,
    }

    return render(request, 'polihack_site/add_subject.html', context)


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