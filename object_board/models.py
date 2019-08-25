import csv
from django.db import models
from django.conf import settings
from django.urls import reverse

class Food(models.Model):
    kind = models.TextField()
    name = models.TextField()
    standard = models.TextField()
    kcal = models.TextField()

    def __str__(self):
        return f'{self.name}'

class METs(models.Model):
    power = models.TextField()
    name = models.TextField()
    mets = models.TextField()

    def __str__(self):
        return f'{self.name}'

class ObPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    count = models.IntegerField(default=0)
    goal = models.CharField(max_length=100)
    finish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('object_board:post_detail', args=[self.pk])

    @property
    def update_counter(self):
        self.count = self.count + 1
        self.save()
        return ""

class ObjComment(models.Model):
    post = models.ForeignKey(ObPost, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)