import os
import secrets
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from rest_framework.response import Response
from user.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .crypto import Crypto
from .models import Secret


class RecoverPassword(APIView): 

    link = os.environ.get('HOST_FRONT')

    def post(self, request, *args, **kwargs): # Recibe un email lo busca y si se encuentra le envia el link de restauración al correo

        try:
            email = request.data['email']
            email = User.objects.filter(email=email).values('email')[0]['email']
            token = secrets.token_urlsafe(20)
            url = f'{self.link}/email-recover?token={token}'
            
            send_mail(
                'Recuperación de contraseña.',
                f'Por favor ingrese a este link {url} para reestablecer su contraseña.',
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            Secret(token=token).save()
            
            return Response(
                {
                    'message':f'Se va enviado un link al correo {Crypto.encrip_email(email)} con los pasos para restaurar su contraseña.'
                },
                    status=HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    {
                        'message':'Lo sentimos no tiene ningun correo registrado, comuniquese con el area de soporte!',
                    },
                status=HTTP_400_BAD_REQUEST
            )


    def get(self, request, *args, **kwargs):

        token = request.query_params.get('token')

        return Response({
            'message': str(token),
            
        }, status=HTTP_200_OK)