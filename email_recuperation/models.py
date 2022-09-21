from django.db import models

# Create your models here.

class Secret(models.Model):
    token = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.token