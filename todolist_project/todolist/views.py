from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from todolist.serializer import *
from django.contrib.auth.models import User
# Create your views here.

class LoginViewSet(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer  

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class TodolistViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]