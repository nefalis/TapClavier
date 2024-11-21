from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SubProfile


class UserSerializer(serializers.ModelSerializer):
    sub_profiles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'sub_profiles', 'date_joined']
        read_only_fields = ['date_joined']


class SubProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProfile
        fields = ['id', 'user', 'username', 'score', 'progress', 'created_at']
        read_only_fields = ['created_at']
