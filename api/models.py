from django.db import models

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    img = models.ImageField(upload_to='img/pets/')
    age = models.IntegerField(default=1)
    sex = models.CharField(max_length=10, default='Macho')
    size = models.IntegerField(default=1)
    city = models.CharField(max_length=66, default='Miami')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

# Test
class ModelPetTest(models.Model):
    name = models.CharField(max_length=10)
    img = models.ImageField(upload_to='img/petstes/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name