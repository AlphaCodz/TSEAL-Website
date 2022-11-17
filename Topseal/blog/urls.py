from django.urls import path, re_path
from . import views
from .views import index

app_name = "webadmin"

urlpatterns = [
    # path('index/', ArticleListView.as_view, name="index"),
    path('index/', views.index, name="index"),
    path('author/', views.author, name="index")
]
