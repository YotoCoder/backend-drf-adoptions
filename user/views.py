from rest_framework import viewsets
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.core.mail import send_mail
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.conf.global_settings import EMAIL_HOST_USER


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer

    # encriptar password en el patch y el put 

class UserRegister(APIView):
    """
    Recive una petición POST y registra un nuevo usuario
    los datos del usuario se reciben en el body de la petición
    en formato JSON, se valida que el email no exista en la base de datos
    y se envia un correo de bienvenida al usuario.

    {
        "password": "password",
        "username": "username",
        "email": "nombre@gmail.com",
        "phone": "925119585"
    }
    
    queda pendiente agrega confirmación al usuario con un link de verificación.

    """

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():    
            email = serializer.validated_data['email']
            if User.objects.filter(email=email).exists():
                return Response({'message': 'Este email ya está registrado'}, status=HTTP_400_BAD_REQUEST)
            else:
                try:
                    
                    send_mail(
                    'Bienvenido a adoptame.ga',
                    'Gracias por registrarte en adoptame.ga.',
                    EMAIL_HOST_USER,
                    [email],
                    fail_silently=False
                    )
                    user = serializer.save()
                    user.set_password(user.password)
                    user.save()
                    return Response({'message': 'Usuario registrado correctamente 😊!'}, status=HTTP_200_OK)
                except:
                    return Response({'message': 'Error al enviar el correo de verificación 😔'}, status=HTTP_400_BAD_REQUEST)
                
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


     
class UserUpdateData(APIView):
    """
    Recive una petición PATCH y actualiza los datos del usuario
    los datos del usuario se reciben en el body de la petición
    en formato JSON, se valida que el email no exista en la base de datos
    y se envia un correo de bienvenida al usuario.

    {
        "password": "password",
        "username": "username",
        "email": "
        "phone": "925119585"
    }

    """
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, format=None) -> Response:
        """
        Al hacer una petición PATCH, actualiza los datos del usuario
        Parametros -> recibe el token de autenticación en el header de la petición
        """

        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            # encript password
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response({'message': 'Datos actualizados correctamente 😊!'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


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

