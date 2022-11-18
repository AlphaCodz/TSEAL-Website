from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import DetailView, ListView

# Create your views here.
def author(request):
    return render(request, 'author.html')

class Home(ListView):
    model = Article
    template_name = "home.html"
    ordering = "published_at"
    
class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context

    
