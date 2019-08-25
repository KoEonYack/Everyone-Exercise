from django.conf import settings
from django.db import models
from django.urls import reverse
import csv

class Info(models.Model):
    name = models.TextField()
    address = models.TextField()
    post_number = models.CharField(max_length=7)
    homepage = models.TextField()
    number = models.TextField()
    introduce = models.TextField()
    count = models.IntegerField(default=0)
    rate_sum = models.IntegerField(default=0)
    rate_ave = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name}'

class Map_Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    RATE_CHOICES = (
        ('★☆☆☆☆', '★☆☆☆☆'),
        ('★★☆☆☆', '★★☆☆☆'),
        ('★★★☆☆', '★★★☆☆'),
        ('★★★★☆', '★★★★☆'),
        ('★★★★★', '★★★★★'),
    )
    rate = models.CharField(max_length=5, choices=RATE_CHOICES)
    message = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
