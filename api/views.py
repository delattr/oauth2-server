from django.shortcuts import render
from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserDetailSerializer

CustomUser = get_user_model()

class UserList(generics.ListCreateAPIView):
    """ List all users"""

    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    """ User detail view.  returns email, first name and last name"""

    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'email'