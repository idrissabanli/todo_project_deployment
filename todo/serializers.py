from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title',]