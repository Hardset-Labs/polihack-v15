import uuid

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory
from .forms import SubjectForm, LearningMinutesDayForm
from .models import UserData, Subject, LearningMinutesDay, Chapter, Question
from datetime import date

LearningMinutesDayFormSet = formset_factory(LearningMinutesDayForm, extra=1)


# Create your views here.
def home(request):
    subject_today = get_today_subjects(request)
    print(subject_today)

    return render(request, 'polihack_site/home.html',
                  {'user_data': return_user(request), 'subject_today': subject_today})


def get_today_subjects(request):
    # get the user data
    user_id = return_user(request).id
    # get the subjects for the user
    subjects = Subject.objects.all().filter(user=user_id)
    # get the current date
    today = date.today()
    # get the learning minutes for the day for each subject and pair them with the subject
    subject_today = []
    try:
        for subject in subjects:
            learning_minutes = LearningMinutesDay.objects.all().filter(subject=subject, date=today)
            subject_today.append((subject, learning_minutes))
        # remove the subjects that have no learning minutes
        subject_today = [subject for subject in subject_today if subject[1]]
    except:
        pass
    return subject_today


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


def study_plan(request, subject_id):
    return render(request, 'polihack_site/study_plan.html',
                  {'user_data': return_user(request), 'subject': Subject.objects.get(id=subject_id),
                   'chapters': Chapter.objects.all().filter(subject=subject_id)})


def get_user_data(request):
    # Create a new user based on session
    return render(request, 'polihack_site/base.html', {'user_data': return_user(request)})


def return_user(request):
    if 'user' not in request.session:
        # Generate a unique username using UUID
        username = str(uuid.uuid4())[:8]  # Generate a UUID and take the first 8 characters as the username
        request.session['user'] = username
        user_data = UserData(user=username)
        user_data.save()
    else:
        user_data = UserData.objects.get(user=request.session['user'])
    return user_data


def get_subjects(request):
    # Create some mock subjects
    user_id = return_user(request).id
    subjects = Subject.objects.all().filter(user=user_id)
    if request.user.is_superuser:
        subjects = Subject.objects.all()
    return render(request, 'polihack_site/subjects.html', {'subjects': subjects, 'user_data': return_user(request)})


def edit_subject(request, subject_id):
    # pull by id the subject and give it to the template
    subject = get_object_or_404(Subject, id=subject_id)
    return render(request, 'polihack_site/add_subject.html', {'subject': subject})


def delete_subject(request, subject_id):
    # delete the subject
    userdata = return_user(request)
    subject = get_object_or_404(Subject, id=subject_id)
    subject.delete()
    return redirect('subjects')


def learn_now(request):
    # get the first subject
    try:
        subject_today = get_today_subjects(request)[0]
    except:
        return redirect('home')
    if not subject_today:
        return redirect('home')
    # get the first unlearned chapter
    return learn_subject(request, subject_today[0].id)


def learn_subject(request, subject_id):
    # get the subject
    subject = Subject.objects.get(id=subject_id)
    print(subject.name)
    # get the chapters
    chapters = Chapter.objects.all().filter(subject=subject_id)
    print(chapters)
    # get the first unlearned chapter
    for chapter in chapters:
        if chapter.progress != 100:
            # get the first question
            first_question = Question.objects.all().filter(chapter=chapter)[0]
            return render(request, 'polihack_site/learn.html',
                          {'user_data': return_user(request), 'subject': subject, 'chapter': chapter,
                           'question': first_question, 'subject_id': subject_id})
    return redirect('home')

def loading_page(request):
    return render(request, 'loading_page.html')

