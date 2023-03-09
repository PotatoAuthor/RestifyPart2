from django.shortcuts import render
from rest_framework.serializers import ModelSerializer
from django.conf import settings
from .models import CustomUser
from django.contrib.auth import get_user_model

# Create your views here.

class UserSerializer(ModelSerializer):
    
    class Meta:
        User = get_user_model()
        model = User
        fields = ['first_name', 'last_name', 'username', 'avatar', 'password', 'phone_num', 'email', 'birth_date']

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create_user(**validated_data)
        return user