from django.db import models
from django.conf import settings
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Ad_Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    count = models.IntegerField(default=0)
    photo = models.ImageField(blank=True, null=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120, 60)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('ad_post:post_detail', args=[self.pk])

    @property
    def update_counter(self):
        self.count = self.count + 1
        self.save()
        return ""

class Ad_Comment(models.Model):
    post = models.ForeignKey(Ad_Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)