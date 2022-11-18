from django.urls import path, re_path
from . import views
from .views import Home, ArticleDetailView

app_name = "blog"

urlpatterns = [
    path('home/', Home.as_view(), name="home"),
    path('author/', views.author, name="index"),
    re_path('article/<int:id>/', ArticleDetailView.as_view(), name="article_details")
]
