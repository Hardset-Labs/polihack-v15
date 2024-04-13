from django.contrib import admin

# Register your models here.

from .models import UserData, Subject, LearningMinutesDay, Chapter

admin.site.register(UserData)
admin.site.register(Subject)
admin.site.register(LearningMinutesDay)
admin.site.register(Chapter)

