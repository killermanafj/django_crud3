from django import forms
from .models import NewPost

class NewPostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ('author', 'title', 'photo', 'text')