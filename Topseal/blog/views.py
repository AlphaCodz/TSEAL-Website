from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import DetailView, ListView, TemplateView

# Create your views here.
# HOME PAGE
class HomePage(ListView):
    model= Article
    template_name = "article_list.html"
    
# Latest Article page
class LatestArticlePage(ListView):
    model= Article
    template_name = "webadmin/latest.html"
    
    def get_queryset(self):
        return Article.objects.all().order_by("-published_at")
    
# Article contents page
class Details(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "articles"

# # Authors Profile Page
# class AuthorDetails(DetailView):
#     model = Article
#     template_name = "author.html"
#     context_object_name = "author"




