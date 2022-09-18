from rest_framework import viewsets, permissions
from .models import Pet

from .serializers import PetSerializer

class PetView(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetSerializer
