import os
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from rest_framework.response import Response
from user.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .crypto import Crypto




# Recibe un email lo busca y si se encuentra le envia el link de restauración al correo

class RecoverPassword(APIView):

    link = os.environ.get('HOST')

    def post(self, request):

        try:
            email = request.POST['email']
            email = User.objects.filter(email=email).values('email')[0]['email']

            send_mail(
                'Recuperación de contraseña.',
                f'Por favor ingrese a este link {self.link} para reestablecer su contraseña.',
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response(
                {
                    'message':f'Se va enviado un link al correo {Crypto.encrip_email(email)} con los pasos para restaurar su contraseña.'
                },
                    status=HTTP_200_OK
            )
        except Exception as e:
            return Response(
                    {
                        'message':'Lo sentimos no tiene ningun correo registrado, comuniquese con el area de soporte!'
                    },
                status=HTTP_400_BAD_REQUEST
            )