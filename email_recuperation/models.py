from django.db import models

# Create your models here.

class Secret(models.Model):
    key = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

