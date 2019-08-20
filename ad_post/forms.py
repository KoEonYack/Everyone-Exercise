from django import forms
from .models import Ad_Comment, Ad_Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Ad_Comment
        fields = ['message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Ad_Post
        fields = ['title', 'photo', 'content']
