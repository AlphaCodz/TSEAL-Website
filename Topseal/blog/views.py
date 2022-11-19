from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import DetailView, ListView, TemplateView

# Create your views here.
class HomePage(ListView):
    model= Article
    template_name = "webadmin/article_list.html"
    
    def get_queryset(self):
        return Article.objects.all().order_by("-published_at")

class Details(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "articles"
    


