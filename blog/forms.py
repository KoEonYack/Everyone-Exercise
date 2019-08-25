from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        #fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'sport', 'location', 'people', 'duration', 'finish']
