from django.contrib import admin
from .models import MyUser, Article

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Article)
