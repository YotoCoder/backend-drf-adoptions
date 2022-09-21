from django.db import models

# Create your models here.

class Key(models.Model):
    is_active = models.BooleanField()
    