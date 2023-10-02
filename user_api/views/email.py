from rest_framework import viewsets

from user_api.models.email import Email
from user_api.serializers.email import EmailSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
