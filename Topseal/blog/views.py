from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import DetailView

# Create your views here.
def author(request):
    return render(request, 'author.html')

class index(DetailView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article'