from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager
from django.urls import reverse
from ckeditor.fields import RichTextField
# from sorl.thumbnail import get_thumbnail


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
class MyUser(AbstractUser):
    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    profile_image = models.ImageField(upload_to="profile_images/", null=True)
    email = models.EmailField(unique=True)
    writer = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Article(models.Model):
    title = models.CharField(max_length=300, unique=True)
    author = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    description_image = models.ImageField(upload_to="article_images/", null=True)
    image_description = models.CharField(max_length=100, null=True)
    content = RichTextField(blank=True,  null=True)
    tag1 = models.CharField(max_length=100, null=True)
    tag2 = models.CharField(max_length=100, null=True)
    tag3 = models.CharField(max_length=100, null=True)
    published_at = models.DateTimeField(auto_now_add=True, null=True)
    featured = models.BooleanField(default=False, null=True)
    top_story = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return f"Title: {self.title}  ||  Author: {self.author.first_name} {self.author.last_name}"
    
    def get_absolute_url(self):
        return reverse("article_details", args=(int(self.id),))
   
    