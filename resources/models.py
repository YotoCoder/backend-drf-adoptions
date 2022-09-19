from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/resources/')

    def __str__(self) -> str:
        return self.name