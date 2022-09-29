from django.db import models
from user.models import User

# Create your models here.

class Secret(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    
    def __str__(self):
        return self.token