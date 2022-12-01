from django.urls import path, re_path, reverse
from . import views
from .views import HomePage, Details, LatestArticlePage, ContentDetails, TopNews

app_name = "blog"

urlpatterns = [
    path("home/", HomePage.as_view(), name="index"),
    re_path(r"^latest/$",LatestArticlePage.as_view(), name="latest"),
    re_path(r'^home/(?P<pk>\d+)/$', Details.as_view(), name='book-detail'),
    re_path(r'latest/(?P<pk>\d+)/$', ContentDetails.as_view(), name="content-details"),
    re_path(r'create/article/', views.CreateArticle,name="create"),
    re_path(r'topnews/', TopNews.as_view(), name="topnews")
]
