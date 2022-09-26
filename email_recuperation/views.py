import os
import secrets
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from rest_framework.response import Response
from user.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from helpers.crypto import Crypto
from .models import Secret


class RecoverPassword(APIView): 

    link = os.environ.get('HOST_FRONT')

    def get(self, request, *args, **kwargs):
        """
        Recibe un token y si se encuentra en la base de datos
        envia un link de restauración de contraseña al email                                              
        """

        token = request.query_params.get('token')

        if Secret.objects.filter(token=token):

            token = Secret.objects.filter(token=token)
            user_id = token.values()[0]['user_id']
            user_name = User.objects.filter(id=user_id).values('username')[0]['username']
            token.delete()

            return Response({
                'accept': True,
                'username': user_name
            }, status=HTTP_200_OK)
        else:
            return Response({
                'accept': False,
                'message': 'Parece que su link a expirado, vuelva a solicitar uno.',
                'url': f'{self.link}/email-recover'
                
            }, status=HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
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


    def patch(self, request, *args, **kwargs):
        """
        Actualiza la contraseña del usuario
        Recibe el username y la nueva contraseña
        params: username, password
        """
        try:
            username = request.data['username']
            password = request.data['password']
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return Response({
                'message': 'Contraseña actualizada correctamente.'
            }, status=HTTP_200_OK)
        except Exception as e:

            return Response({
                'message': 'Lo sentimos no se pudo actualizar su contraseña, comuniquese con el area de soporte.'

            }, status=HTTP_400_BAD_REQUEST)