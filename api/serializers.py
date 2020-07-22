from django.db import transaction
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Organizer, Person


# ANDRES CODE
class PersonSerializer(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = Person
        fields = ("about",)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    person = PersonSerializer()
    class Meta:
        model = User
        fields = ('id','username', 'password','first_name', 'last_name', "email", "person",)
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    


# BORIS CODE
class OrganizerSerializer(serializers.Serializer):
 
    id          = serializers.IntegerField(read_only=True)
    email       = serializers.EmailField(max_length=50)
    password    = serializers.CharField(min_length=8)
   

    def create(self,validated_data):
        
        """
        Create and return a new `Organizer` instance, given the validated data.
        """
        organizer = Organizer.objects.create(**validated_data) 
        token = Token.objects.create(user=organizer)
        return organizer
        
        
    def update(self, instance, validated_data):
        """
        Update and return an existing `Organizer` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']