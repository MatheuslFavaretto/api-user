from rest_framework import viewsets

from user_api.models.user import User
from user_api.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
