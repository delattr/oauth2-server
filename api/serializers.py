from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


class CreateUserSerializer(serializers.ModelSerializer):
    """ Create User by email and password """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

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