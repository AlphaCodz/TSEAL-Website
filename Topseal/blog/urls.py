from django.urls import path, re_path
from . import views
from .views import HomePage, Details

app_name = "blog"

urlpatterns = [
    # path("", views.HomePage, name="view")
    path("", HomePage.as_view(), name="index"),
    re_path(r'^(?P<pk>\d+)/$', Details.as_view(), name='book-detail'),
]
