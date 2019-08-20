from django import forms
from .models import Map_Comment

class PostSearchForm(forms.Form):
    search_word = forms.CharField(
        label='Search Word',
        widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "input",
            "placeholder": "Input here",
    }))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Map_Comment
        fields = ['message']
        #fields = '__all__'