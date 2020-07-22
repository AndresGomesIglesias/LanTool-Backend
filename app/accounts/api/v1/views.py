from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from app.accounts.models import Profile, Club
from app.accounts.api.v1.serializers import (
    UserSerializer,
    UserUpdateSerializer,
    AvatarSerializer,
    ClubSerializer
)


class UserCreatView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        return User.objects.all()
      
class UserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        return User.objects.all()
 
class AvatarAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = AvatarSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        return Profile.objects.all()

class GetAuthToken(ObtainAuthToken):
    def post(self , request, *args, **kwargs):
        response = super(GetAuthToken, self).post(request,*args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        user_serializer = UserSerializer(user, many=False, context={'request': request})
        return Response({'token': token.key, 'user': user_serializer.data})
      


    
class ClubAPIView(generics.ListCreateAPIView):
    serializer_class = ClubSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Club.objects.all()
