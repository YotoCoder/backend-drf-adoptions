from django.contrib import admin
from .models import ModelPetTest, Pet

# Register your models here.

admin.site.register(Pet)
admin.site.register(ModelPetTest)