from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.views.generic import DetailView, ListView, TemplateView
from .forms import ArticleForm

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

# Authors Profile Page
class ContentDetails(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "articles"
    
def CreateArticle(request):
    if request.method == "POST":
        article = ArticleForm(data=request.POST)
        if article.is_valid():
            articles = article.save()
            articles.save()
            
        if 'description_image' in request.FILES:
            article.description_image = request.FILES['description_image']
            article.save()
        else:
            return article.errors
    else:
        article = ArticleForm()
    return render(request, 'create_article.html')


class TopNews(ListView):
    model = Article
    template_name = "webadmin/topnews.html"
    
    def get_queryset(self):
        return Article.objects.filter(top_story=True)