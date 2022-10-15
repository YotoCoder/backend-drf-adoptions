from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('create_at',)

        # VALORES MINIMOS PARA EL REGISTRO DE UN USUARIO
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 4},
            'username': {'min_length': 4},
            'first_name': {'min_length': 4},
            'last_name': {'min_length': 4},
            'email': {'min_length': 9},
            'phone': {'min_length': 9},
        }