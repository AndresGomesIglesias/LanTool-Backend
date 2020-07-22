from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import Organizer, Person
from .serializers import OrganizerSerializer, UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]



class GetAuthToken(ObtainAuthToken):
    
    def post(self , request, *args, **kwargs):
        response = super(GetAuthToken, self).post(request,*args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        user_serializer = UserSerializer(user, many=False)
        return Response({'token': token.key, 'user': user_serializer.data})
      


  

# BORIS CODE
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    

 

@csrf_exempt
def organizer_list(request):
    """
    List all organizers info
    """
    if request.method == 'GET':
        organizers = Organizer.objects.all()
        serializer = OrganizerSerializer(organizers,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrganizerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def organizer_detail(request,pk):
    """
    Retrieve, update or delete an organizer
    """
    try:
        organizer = Organizer.objects.get(pk=pk)
    except Organizer.DoesNotExist:
        return HttpResponse("<h1>Error, this organizer does not exist</h1>")
    if request.method == 'GET':
        serializer = OrganizerSerializer(organizer)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrganizerSerializer(organizer,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        organizer.delete()
        return HttpResponse(status=204)





