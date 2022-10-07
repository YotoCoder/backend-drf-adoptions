from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from email_recuperation.views import RecoverPassword

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Adoptions API",
      default_version='v1',
      description="Documentacion de la API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="yotoelectronics@gmail.com"),
      license=openapi.License(name="GNU"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urls.urls')),

    # Auth routes
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Email recover test
    path('email-recover/', RecoverPassword.as_view(), name='recover-password'),

    # documentación
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Debug toolbar
    path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)