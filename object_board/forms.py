from django import forms
from .models import ObjComment, ObPost

class FoodSearchForm(forms.Form):
    search_food = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "input",
                "placeholder": "음식 이름을 입력해 주세요",
            }))

class CommentForm(forms.ModelForm):
    class Meta:
        model = ObjComment
        fields = ['message']
        #fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = ObPost
        fields = ['title', 'content', 'finish']
