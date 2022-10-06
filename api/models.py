from django.db import models
from user.models import User

# Create your models here.

CHOICES_AGE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)

CHOICES_SEX = (
    ('Macho', 'Macho'),
    ('Hembra', 'Hembra'),
)

CHOICES_SIZE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)

CHOICES_TYPE_PET = (
    ('Perro', 'Perro'),
    ('Gato', 'Gato'),
    ('Otro', 'Otro'),
)

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    img = models.ImageField(upload_to='img/pets/')
    age = models.CharField(max_length=1, choices=CHOICES_AGE)
    sex = models.CharField(max_length=10, choices=CHOICES_SEX)
    size = models.CharField(max_length=1, choices=CHOICES_SIZE)
    type_pet = models.CharField(max_length=10, choices=CHOICES_TYPE_PET)
    city = models.CharField(max_length=66, default='Lima')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name