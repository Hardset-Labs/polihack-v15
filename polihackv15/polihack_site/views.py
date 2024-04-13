from datetime import date
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

def subjects(request):
    # Create some mock subjects
    subjects_data = [
        {"name": "Math", "start_date": date(2024, 4, 1), "end_date": date(2024, 4, 30), "pdf_files": "math_notes.pdf", "video_files": "math_video.mp4", "progress": 30},
        {"name": "History", "start_date": date(2024, 4, 15), "end_date": date(2024, 5, 15), "pdf_files": "history_notes.pdf", "video_files": "history_video.mp4", "progress": 50},
        {"name": "Science", "start_date": date(2024, 4, 20), "end_date": date(2024, 5, 20), "pdf_files": "science_notes.pdf", "video_files": "science_video.mp4", "progress": 20},
        {"name": "English", "start_date": date(2024, 4, 10), "end_date": date(2024, 5, 10), "pdf_files": "english_notes.pdf", "video_files": "english_video.mp4", "progress": 40},
        {"name": "Geography", "start_date": date(2024, 4, 5), "end_date": date(2024, 5, 5), "pdf_files": "geography_notes.pdf", "video_files": "geography_video.mp4", "progress": 60},
        {"name": "Biology", "start_date": date(2024, 4, 25), "end_date": date(2024, 5, 25), "pdf_files": "biology_notes.pdf", "video_files": "biology_video.mp4", "progress": 70},
        {"name": "Physics", "start_date": date(2024, 4, 12), "end_date": date(2024, 5, 12), "pdf_files": "physics_notes.pdf", "video_files": "physics_video.mp4", "progress": 80},
    ]

    # Create Subject objects from the mock data
    subjects = []
    for subject_data in subjects_data:
        subject = Subject.objects.create(
            name=subject_data["name"],
            start_date=subject_data["start_date"],
            end_date=subject_data["end_date"],
            pdf_files=subject_data["pdf_files"],
            video_files=subject_data["video_files"],
            progress=subject_data["progress"],
            #user=request.user  # Assuming you have a logged-in user and want to assign the subjects to this user
        )
        subjects.append(subject)

    return render(request, 'polihack_site/subjects.html', {'subjects': subjects})