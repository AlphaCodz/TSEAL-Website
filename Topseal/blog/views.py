from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import DetailView, ListView

# Create your views here.
def author(request):
    return render(request, 'author.html')

def index(request):
    article = Article.objects.all().order_by("-published_at")
    
    context = {
        "article": article
    }
    return render(request, 'index.html', context=context)

# class ArticleListView(ListView):
#     model = Article
#     def head(self, *args, **kwargs):
#         last_article = self.get_queryset().latest('published_at')
#         response = HttpResponse(
        
#             headers={'Last-Modified': last_article.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')},
#         )
#         return response