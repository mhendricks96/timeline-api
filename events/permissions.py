from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
  
  def has_object_permission(self, request, view, object):

    if request.method in permissions.SAFE_METHODS:
      return True

    if object.user is None:
      return True

    return object.user == request.user

class AllowAny(permissions.BasePermission):

  def has_object_permission(self, request, view, object):
    return True
