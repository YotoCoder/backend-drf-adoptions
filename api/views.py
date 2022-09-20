from rest_framework import viewsets, permissions
from .models import Pet, ModelPetTest

from .serializers import PetSerializer, PetTestSerializer

class PetView(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PetSerializer

class PetTestView(viewsets.ModelViewSet):
    queryset = ModelPetTest.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PetTestSerializer