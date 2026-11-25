import datetime
from django.contrib import admin
from django.utils import timezone
from django.db import models

from django.conf import settings

# Create your models here.
class Question(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    

    def __str__(self):
        return self.question_text

    
    
    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        super().save_model(request, obj, form, change)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text