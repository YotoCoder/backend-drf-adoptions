from rest_framework import serializers

from .models import Pet, ModelPetTest

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
        read_only_fields = ('create_at',)

class PetTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPetTest
        fields = '__all__'
        read_only_fields = ('create_at',)