from django.forms import ModelForm
from django import forms
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ("title", "author", "image_description", "description_image", "content", "featured", "top_story")
         