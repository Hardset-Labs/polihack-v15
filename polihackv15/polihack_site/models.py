from django.db import models


# Create your models here.


class UserData(models.Model):
    user = models.CharField(max_length=100)
    lives = models.IntegerField(default=3)
    streak = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta: 
        app_label = 'polihack_site'
    
    def _init_(self, user, lives=3, streak=0, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.user = user
        self.lives = lives
        self.streak = streak


class Subject(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(UserData, on_delete=models.CASCADE, default="1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pdf_files = models.FileField(upload_to='pdf_files/', null=True, blank=True)
    video_files = models.FileField(upload_to='video_files/', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    generated = models.BooleanField(default=False)
    generated_at = models.DateTimeField(null=True, blank=True)
    progress = models.IntegerField(default=0)

    def _str_(self):
        return self.name


class LearningMinutesDay(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    minutes = models.IntegerField()

    def _str_(self):
        return self.subject.name + " " + str(self.date) + " " + str(self.minutes) + " minutes"


class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    summary = models.TextField()
    progress = models.IntegerField(default=0)
    got_correct_total = models.IntegerField(default=0)
    got_wrong_total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name


class Question(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    question = models.TextField()
    dummy_answer1 = models.TextField()
    dummy_answer2 = models.TextField()
    dummy_answer3 = models.TextField()
    correct_answer = models.TextField()
    explanation = models.TextField()
    active = models.BooleanField(default=True)
    got_correct = models.IntegerField(default=0)
    got_wrong = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.question