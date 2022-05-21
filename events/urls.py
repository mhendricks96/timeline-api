from django.urls import path
from .views import EventList, EventDetail, CommentList, CommentDetail, UserTimelineList, UserTimelineDetail, UserList, UserDetail, UserCreate

urlpatterns = [
  path('events/', EventList.as_view(), name='event_list'),
  path('event/<int:pk>/', EventDetail.as_view(), name='event_detail'),
  path('comments/', CommentList.as_view(), name='comment_list'),
  path('comment/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
  path('timelines/', UserTimelineList.as_view(), name='timeline_list'),
  path('timeline/<int:pk>/', UserTimelineDetail.as_view(), name='timeline_detail'),
  path('users/', UserList.as_view()),
  path('users/<int:pk>/', UserDetail.as_view()),
  path('create_user/', UserCreate.as_view()),
]