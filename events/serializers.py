from rest_framework import serializers
from .models import Event, Comment, UserTimeline
from django.contrib.auth.models import User
from django.utils.html import escape

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('title', 'description', 'date', 'likes', 'category')
    model = Event

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('words', 'event_posted_on', 'user', 'created_at', 'updated_at')
    model = Comment

class UserTimelineSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('user', 'year', 'categories')
    model = UserTimeline

class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
      password = validated_data.pop('password')
      user = super().create(validated_data)
      user.set_password(password)
      user.save()
      return user
    
    def validate_myfield(self, value):
      return escape(value)

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
      password = validated_data.pop('password')
      user = super().create(validated_data)
      user.set_password(password)
      user.save()
      return user

    def validate_myfield(self, value):
      return escape(value)