from django.forms import ModelForm
from django import forms
from .models import Article

class ArticleForm(ModelForm):
    description_image = forms.ImageField(max_length=500, required=True)
    class Meta:
        model = Article
        fields = "__all__"
         