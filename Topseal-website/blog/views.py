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
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
                        
            return redirect('/home')
        else:
            print(form.errors.as_data())
    form = ArticleForm()
    context = {"form":form}
    return render(request, 'create_article.html', context)