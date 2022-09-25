from rest_framework import viewsets, permissions, generics
from .models import Pet, ModelPetTest
from .serializers import PetSerializer, PetTestSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PetView(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['age', 'sex', 'size']

class PetTestView(viewsets.ModelViewSet):
    queryset = ModelPetTest.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetTestSerializer


# Crear una vista con el endpoint /api/pet/filter que permita filtrar con rangos de edad, sexo y tamaño

class PetFilterView(generics.ListAPIView):
    queryset = Pet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'age': ['gte', 'lte',],
        'sex': ['contains'],
        'size': ['gte', 'lte']
    }