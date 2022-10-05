from rest_framework import viewsets, permissions
from .models import Pet
from .serializers import PetSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response


class PetView(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        'age': ['gt', 'lt', 'exact'],
        'sex': ['exact'],
        'size': ['gt', 'lt', 'exact'],
        'owner': ['exact'],
        'city': ['contains'],
    }


    # Create view
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def test_view(self, request):

        return Response({'test': 'test'})