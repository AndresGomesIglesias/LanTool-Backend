from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from app.accounts.models import Profile, Club



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            # "id",
            "avatar",
            "description",
            )


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'avatar',
            )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile     = ProfileSerializer()
    email       = serializers.EmailField(max_length=50, required=True)
    password    = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            "email",
            "profile",
            )
        extra_kwargs = {
            'password': {
                'write_only': True, 
                'required': True,
                },
            } 



    @transaction.atomic
    def create(self, validated_data): 
         profile_data = validated_data.pop('profile')
         user = User.objects.create_user(**validated_data)
         token = Token.objects.create(user=user)
         user.profile = Profile.objects.create(user=user, **profile_data)
         user.save()
         return user

class UserUpdateSerializer(serializers.HyperlinkedModelSerializer):
    profile      = ProfileSerializer()
  
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            "email",
            "profile",
            )
       
    
    @transaction.atomic
    def update(self, instance, validated_data):
    
        nested_data = validated_data.pop('profile')
        self.fields['profile'].update(instance.profile, nested_data)
     
        for key in validated_data:
            setattr(instance, key, validated_data[key])

        instance.save()
        return instance

class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = ('__all__')

  