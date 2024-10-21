from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=128, default='Guest')
    email = models.EmailField(max_length=256, unique=True)
    username = None
    phone = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    session_token = models.CharField(max_length=64, default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Django Inherited field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    