from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# This is how we sign in with a bearer token from the react front end

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    # Add custom claims
    token['email'] = user.email
    token['username'] = user.username

    return token


class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer
