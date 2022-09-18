from rest_framework.routers import DefaultRouter
from .views import PetView

router = DefaultRouter()

router.register('api/pet', PetView, 'petview')

urlpatterns = router.urls