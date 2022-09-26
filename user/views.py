from rest_framework import viewsets
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.core.mail import send_mail
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import secrets
from django.conf.global_settings import EMAIL_HOST_USER
from helpers.crypto import Crypto

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


class UserView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        """
        Al hacer una petición POST, regresa los datos del usuario
        Parametros -> recibe el token de autenticación en el header de la petición
        """

        content = {
            'id': str(request.user.id),
            'user': str(request.user.username),
            'phone': str(request.user.phone),
            'email': str(request.user.email),
            'first_name': str(request.user.first_name),
            'last_name': str(request.user.last_name),
            'is_staff': str(request.user.is_staff),
            'is_active': str(request.user.is_active),
            'is_superuser': str(request.user.is_superuser),
            'date_joined': str(request.user.date_joined),
        }

        return Response(content)

    def get(self, request, *args, **kwargs):
        """
        Recibe un email y si se encuentra en la base de datos envia un link de restauración de contraseña al email
        """
        try:
            email = request.data['email']
            email = User.objects.filter(email=email).values('email')[0]['email']
            user_id = User.objects.filter(email=email).values('id')[0]['id']
            token = secrets.token_urlsafe(20)
            url = f'{self.link}/email-recover?token={token}'

            send_mail(
                'Recuperación de contraseña.',
                f'Por favor ingrese a este link {url} para reestablecer su contraseña.',
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            Secret(user_id=user_id, token=token).save()
            
            return Response({
                    'message':f'Se va enviado un link al correo {Crypto.encrip_email(email)} con los pasos para restaurar su contraseña.'
            }, status=HTTP_200_OK)

        except Exception as e:
            return Response({
                'message':'Lo sentimos no tiene ningun correo registrado, comuniquese con el area de soporte!',

            }, status=HTTP_400_BAD_REQUEST)


