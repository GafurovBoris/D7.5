from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'categoryType',
            'postCategory',
            'rating',
            'title',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("description")
        title = cleaned_data.get("name")

        return cleaned_data