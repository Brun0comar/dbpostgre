from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import Superheroes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class SuperheroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superheroes
        fields = ['id', 'nick', 'real_name', 'power']

class MyTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

       
        token['is_admin'] = user.is_staff  
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer
