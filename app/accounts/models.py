from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, ImageField

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)
class Profile(TimeStampedModel):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, default=False)
    description = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to=upload_location, null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username

class Club(TimeStampedModel):
    
    name = models.CharField(max_length=100,null=True, blank=True)
    tag = models.CharField(max_length=10,null=True, blank=True)
    web = models.CharField(max_length=250,null=True)
    email = models.EmailField(max_length=50)
    about = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to=upload_location, null=True, blank=True)

    # def __str__(self):
    #     return self.tag

def sorl_delete(**kwargs):
    delete(kwargs['file'])

cleanup_pre_delete.connect(sorl_delete)



    