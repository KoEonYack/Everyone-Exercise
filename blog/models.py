from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, )     # 조회수
    title = models.CharField(max_length=100)     # 제목
    content = models.TextField()                 # 모집 설명
    sport = models.CharField(max_length=100)     # 운동 종목
    location = models.CharField(max_length=100)  # 장소
    people = models.IntegerField(default=0)      # 모집 인원
    duration = models.CharField(max_length=100)  # 운동 날짜
    finish = models.BooleanField(default=False)  # 모집 완료
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

    @property
    def update_counter(self):
        self.count = self.count + 1
        self.save()
        return ""

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)