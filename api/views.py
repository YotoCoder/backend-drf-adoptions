from rest_framework import viewsets, permissions
from .models import Pet
from .serializers import PetSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PetView(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        'age': ['gt', 'lt', 'exact'],
        'sex': ['exact'],
        'size': ['gt', 'lt', 'exact'],

        'city': ['contains'],
    }