from django import forms
from django.forms import formset_factory
from .models import Subject, LearningMinutesDay

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'pdf_files', 'video_files', 'start_date', 'end_date']

class LearningMinutesDayForm(forms.ModelForm):
    class Meta:
        model = LearningMinutesDay
        fields = ['date', 'minutes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

