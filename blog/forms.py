from django import forms
from .models import Blog

class BlogResponseForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['content']
