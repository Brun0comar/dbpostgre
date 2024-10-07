from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Superheroes
from .serializers import SuperheroesSerializer
from rest_framework import generics

class SuperheroesListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        is_admin = request.user.is_staff

        if is_admin:
            message = {'message': 'Información para administradores'}
            queryset = Superheroes.objects.all()
        else:
            message = {'message': 'Información pública'}
            queryset = Superheroes.objects.filter(is_public=True)

        
        serializer = SuperheroesSerializer(queryset, many=True)

        
        return Response({'message': message['message'], 'superheroes': serializer.data})


class SuperheroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Superheroes.objects.all()
    serializer_class = SuperheroesSerializer
