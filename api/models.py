from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, related_name='person', on_delete=models.CASCADE, default=False)
    about = models.TextField(default=False)
    created = models.DateField(auto_now_add=True, null=True)
    
class Userclub(models.Model):
    club_name = models.CharField(max_length=50, default=False)
    tag = models.CharField(max_length=10,default=False)
    site_web = models.CharField(max_length=200, default=False)
    email = models.CharField(max_length=100, default=False)
    about = models.TextField(default=False)
    create = models.DateField(auto_now_add=True, null=True)
    userclub = models.ForeignKey(Person, related_name='personA', on_delete=models.CASCADE, default=False)



class Organizer(models.Model):
    bio = models.CharField(max_length=256, null=True)
    sex = models.CharField(max_length=256, null=True)