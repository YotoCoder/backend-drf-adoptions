from rest_framework import viewsets, permissions, generics
from .models import Pet, ModelPetTest
from .serializers import PetSerializer, PetTestSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PetView(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
    'age': ['gt', 'lt'],
    'sex': ['exact'],
    'size': ['gt', 'lt'],

    'city': ['contains'],
    }

class PetTestView(viewsets.ModelViewSet):
    queryset = ModelPetTest.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetTestSerializer

