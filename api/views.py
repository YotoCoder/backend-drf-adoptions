from rest_framework import viewsets, permissions
from .models import Pet
from .serializers import PetSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from .paginations import PetPagination

class PetView(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = PetPagination

    filterset_fields = {
        'age': ['gt', 'lt', 'exact'],
        'sex': ['exact'],
        'size': ['gt', 'lt', 'exact'],
        'type_pet': ['exact'],
        'owner': ['exact'],
        'city': ['contains'],
    }