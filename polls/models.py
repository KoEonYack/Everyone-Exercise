from django.conf import settings
from django.db import models
from django.urls import reverse
import csv

'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
'''

class Info(models.Model):
    name = models.TextField()
    address = models.TextField()
    post_number = models.CharField(max_length=7)
    homepage = models.TextField()
    number = models.TextField()
    introduce = models.TextField()

    def __str__(self):
        return f'{self.name}'

    #def get_absolute_url(self):
    #   return reverse('polls:SearchFormView.form_valid', args=['search'])

class Map_Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    RATE_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rate = models.CharField(max_length=2, choices=RATE_CHOICES)
    message = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
