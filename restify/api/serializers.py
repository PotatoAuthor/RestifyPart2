from django.shortcuts import render
from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth import get_user_model

# Create your views here.

class UserSerializer(ModelSerializer):
    password2 = CharField(write_only=True, required=True)
    
    class Meta:
        User = get_user_model()
        model = User
        fields = ['first_name', 'last_name', 'username', 'avatar', 'password', 'password2', 'phone_num', 'email', 'birth_date',]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        data = validated_data.pop('password2')
        User = get_user_model()
        user = User.objects.create_user(**validated_data)
        return user
    
class PasswordSerializer(ModelSerializer):
    password2 = CharField(write_only=True, required=True)
    old_password = CharField(write_only=True, required=True)

    class Meta:
        User = get_user_model()
        model = User
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({"password": "Password fields didn't match."})

        return attrs
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class ProfileSerializer(ModelSerializer):
    username = CharField(required=False)

    class Meta:
        User = get_user_model()
        model = User
        fields = ['first_name', 'last_name', 'username', 'avatar', 'phone_num', 'email', 'birth_date',]

    def update(self, instance, validated_data):
        if 'first_name' in validated_data:
            instance.first_name = validated_data['first_name']
        if 'last_name' in validated_data:
            instance.last_name = validated_data['last_name']
        if 'username' in validated_data:
            instance.username = validated_data['username']
        else:
            instance.username = self.context.get('request').user.username
        if 'avatar' in validated_data:
            instance.avatar = validated_data['avatar']
        if 'phone_num' in validated_data:
            instance.phone_num = validated_data['phone_num']
        if 'email' in validated_data:
            instance.email = validated_data['email']
        if 'birth_date' in validated_data:
            instance.birth_date = validated_data['birth_date']
        instance.save()

        return instance