from django.urls import path, re_path
from . import views
from .views import index

app_name = "webadmin"

urlpatterns = [
    path('index/', index.as_view, name="index"),
    path('author/', views.author, name="index")
]
