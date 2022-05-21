from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import EventSerializer, CommentSerializer, UserTimelineSerializer, CreateUserSerializer, UserSerializer
from .models import Event, Comment, UserTimeline
from rest_framework import response, request
from rest_framework import status
# from friendship.models import Friend
from .permissions import isOwnerOrReadOnly, AllowAny
from rest_framework import permissions
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings

# Create your views here.

class EventList(ListCreateAPIView):
  serializer_class = EventSerializer
  queryset = Event.objects.all()

class EventDetail(RetrieveUpdateDestroyAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class CommentList(ListCreateAPIView):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()

class CommentDetail(RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class UserTimelineList(ListCreateAPIView):
  serializer_class = UserTimelineSerializer
  queryset = UserTimeline.objects.all()

class UserTimelineDetail(RetrieveUpdateDestroyAPIView):
  queryset = UserTimeline.objects.all()
  serializer_class = UserTimelineSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserCreate(CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = CreateUserSerializer

class UserList(ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
