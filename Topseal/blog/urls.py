from django.urls import path, re_path
from . import views

app_name = "webadmin"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('author/', views.author, name="index")
]
