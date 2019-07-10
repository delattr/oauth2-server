from django.urls import path, include
from .views import UserList, UserDetails

urlpatterns = [

    path('users/', UserList.as_view()),
    path('users/<str:email>/', UserDetails.as_view()),
]