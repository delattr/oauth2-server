from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    """ Users list serializer"""
    class Meta:
        model = get_user_model()
        fields = ('id', 'email')


class UserDetailSerializer(serializers.ModelSerializer):
    """ User Detail serilalizer """
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'email',
            'first_name', 'last_name',
            'last_login', 'date_joined')
        lookup_field = 'email'