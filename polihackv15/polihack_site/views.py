import uuid

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory

from .chatgpt.chatgpt_answer_parsing import parse_text
from .forms import SubjectForm, LearningMinutesDayForm
from .models import UserData, Subject, LearningMinutesDay, Chapter, Question
from datetime import date, timedelta, datetime
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Subject  # Import your Subject model here

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


def add_subject(request, subject_id=None):
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

            return redirect('add_subject')  # Use the correct namespace and URL name

    else:
        subject_form = SubjectForm()
        minutes_formset = LearningMinutesDayFormSet()

    # create a new subject and add it to the database
    if subject_id:
        subject = Subject.objects.get(id=subject_id)
        subject_form = SubjectForm(instance=subject)
        # get the learning minutes for the subject
        minutes = LearningMinutesDay.objects.all().filter(subject=subject_id)
        # remove those that are outside of the start and end date
        minutes = [minute for minute in minutes if subject.start_date <= minute.date <= subject.end_date]
        # create new ones for the dates that are missing
        for i in range((subject.end_date - subject.start_date).days + 1):
            date = subject.start_date + timedelta(days=i)
            if not any(minute.date == date for minute in minutes):
                minutes.append(LearningMinutesDay(subject=subject, date=date, minutes=20))
        minutes_formset = LearningMinutesDayFormSet(
            initial=[{'date': minute.date, 'minutes': minute.minutes} for minute in minutes])
        # add all the minutes to the database
        # print(minutes_formset)
        minutes_formset.extra = 0
        for minute in minutes:
            minute.save()


    else:
        subject = Subject()
        subject.user = return_user(request)
        subject.start_date = datetime.today()
        subject.end_date = datetime.today() + timedelta(days=1)
        subject.save()

    context = {
        'subject_form': subject_form,
        'minutes_formset': minutes_formset,
        'user_data': return_user(request),
        'subject': subject,
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


def learn_now(request, last_question_id=None):
    # get the first subject
    if request.method == 'POST':
        # Extract submitted answer from POST data
        submitted_answer = request.POST.get('answer')
        question_id = request.POST.get('question_id')
        correct_answer = Question.objects.get(id=question_id).correct_answer

        # Compare submitted answer with correct answer
        is_correct = submitted_answer == correct_answer

        # Get explanation for the correct answer (assuming you have a function for this)
        explanation = Question.objects.get(id=question_id).explanation

        # You can also save the user's answer and its correctness to the database if needed

        # Return JSON response with correctness and explanation
        return JsonResponse({'is_correct': is_correct, 'explanation': explanation})

    try:
        subject_today = get_today_subjects(request)[0]
    except:
        return redirect('home')
    if not subject_today:
        return redirect('home')
    # get the first unlearned chapter
    return learn_subject(request, subject_today[0].id, last_question_id)


def learn_subject(request, subject_id, last_question_id=None):
    # get the subject
    subject = Subject.objects.get(id=subject_id)
    print(subject.name)
    # get the chapters
    chapters = Chapter.objects.all().filter(subject=subject_id)
    print(chapters)
    # get the first unlearned chapter
    try:
        for chapter in chapters:
            if chapter.progress != 100:
                # get the first question
                first_question = None
                if last_question_id is None:
                    first_question = Question.objects.all().filter(chapter=chapter)[0]
                else:
                    last_question = Question.objects.get(id=last_question_id)
                    questions = Question.objects.all().filter(chapter=chapter)
                    for i in range(len(questions)):
                        if questions[i] == last_question:
                            first_question = questions[i + 1]
                            break
                    if first_question is None:
                        print("No more questions in this chapter")
                        continue
                return render(request, 'polihack_site/learn.html',
                              {'user_data': return_user(request), 'subject': subject, 'chapter': chapter,
                               'question': first_question, 'subject_id': subject_id})
    except:
        pass
    return redirect('home')


def save_subject(request):
    if request.method == "POST":
        # Process form data and update or create the subject
        subject_id = request.POST.get("subject_id")
        name = request.POST.get("name")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        try:
            # Try to get the existing subject
            subject = Subject.objects.get(id=subject_id)
            print(f"Existing subject found with ID: {subject_id}")
        except Subject.DoesNotExist:
            # If the subject does not exist, create a new one
            subject = Subject.objects.create(id=subject_id, name=name, start_date=start_date, end_date=end_date)
            print(f"New subject created with ID: {subject_id}")

        subject.name = name
        subject.save()
        print(f"Subject saved successfully: {subject}")

        # Redirect to subjects page or any other URL
        return HttpResponse("Subject saved successfully", status=200)
    else:
        # Return a 404 error if the request method is not POST
        print("Method Not Allowed:", request.method)
        return HttpResponse("Method Not Allowed", status=404)


def loading_page(request):
    return render(request, 'loading_page.html')


def study_plan(request):
    subject_name = request.GET.get('subject_name')
    subject = get_object_or_404(Subject, name=subject_name)
    chapters = Chapter.objects.filter(subject=subject)  # Retrieve chapters related to the subject
    return render(request, 'polihack_site/study_plan.html', {'subject': subject, 'chapters': chapters})
