from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser):
    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        )
    gender = models.CharField(max_length= 10, choices=GENDER_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    middle_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    username = models.CharField(blank=True, max_length=100)
    phone_number = PhoneNumberField(null=True, unique=True)
    verified_email = models.BooleanField(default=False)
    verified_phonenumber = models.BooleanField(default=False, null=True)
    #staff_id = models.UUIDField(unique=True, null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
