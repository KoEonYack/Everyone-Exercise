from django import forms
from .models import Map_Comment

class PostSearchForm(forms.Form):
    search_word = forms.CharField(
        label='',
        widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "input",

            "placeholder": "지명을 입력해 주세요",
        }
        ))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Map_Comment
        fields = ['rate', 'message']
        #fields = '__all__'