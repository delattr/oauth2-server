from django.urls import path, include
from .views import UserList, UserDetails, CreateUser

urlpatterns = [

    path('user/', UserList.as_view()),
    path('user/<str:email>/', UserDetails.as_view()),
    path('create/', CreateUser.as_view()),

]