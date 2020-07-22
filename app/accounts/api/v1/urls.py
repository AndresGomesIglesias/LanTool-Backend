from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from app.accounts.api.v1.views import (
    UserCreatView,
    UserUpdateView,
    GetAuthToken,
    AvatarAPIView,
    ClubAPIView,
)

app_name = 'accounts'



urlpatterns = [
    path('login/', GetAuthToken.as_view(),              name='user-login'),
    path('create/', UserCreatView.as_view(),            name='user-create'),
    path('update/<int:pk>/', UserUpdateView.as_view(),  name='user-update'),
    path('avatar/<int:pk>/', AvatarAPIView.as_view(),   name='user-avatar'),

    path('club/', ClubAPIView.as_view(),                name='club-details')

]
