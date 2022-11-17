from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def author(request):
    return render(request, 'author.html')

def index(request):
    return render(request, 'index.html')