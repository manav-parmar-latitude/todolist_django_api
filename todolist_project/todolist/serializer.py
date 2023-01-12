from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from todolist.models import TodoList
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import json

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields='__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password', 'is_superuser']

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data["password"] = make_password(password)
        instance = super().create(validated_data)
        instance.save()
        return instance

class MyTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        todolists=TodoList.objects.filter(username=self.user)
        data["username"]=self.user.username
        data["firstname"]=self.user.first_name
        data["lastname"]=self.user.last_name
        for todolist in todolists:
            data[f"name-{todolist.id}"]=todolist.name
            data[f"description-{todolist.id}"]=todolist.description
            data[f"date_created-{todolist.id}"]=todolist.date_created
            data[f"completed-{todolist.id}"]=todolist.completed
        return data