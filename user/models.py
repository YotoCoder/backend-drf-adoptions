from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(max_length=20, unique=True, blank=False, null=False)
    is_active = models.BooleanField(default=False)