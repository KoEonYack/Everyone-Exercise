from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ['title']

@admin.register(Comment)
class PostComment(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at']
    list_display_links = ['post', 'author']