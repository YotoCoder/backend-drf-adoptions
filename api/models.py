from django.db import models

# Create your models here.

CHOICES_AGE = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
)

CHOICES_SEX = (
    ('Macho', 'Macho'),
    ('Hembra', 'Hembra'),
)

CHOICES_SIZE = (
    (1, 1),
    (2, 2),
    (3, 3),
)

class Pet(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    img = models.ImageField(upload_to='img/pets/')
    age = models.IntegerField(default=1, choices=CHOICES_AGE)
    sex = models.CharField(max_length=10, default=2, choices=CHOICES_SEX)
    size = models.IntegerField(default=2, choices=CHOICES_SIZE)
    city = models.CharField(max_length=66, default='Lima')
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