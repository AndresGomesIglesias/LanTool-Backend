from django.contrib import admin


from app.accounts.models import Profile ,Club 
# Register your models here.
admin.site.register(Profile)
admin.site.register(Club)