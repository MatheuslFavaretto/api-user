from rest_framework import serializers

from user_api.models.email import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('id', 'address')
