from django.utils import timezone
from rest_framework import serializers

from email_model.serializers import EmailSerializer
from cpf_model.serializer import CpfSerializer
from endereco_model.serializer import EnderecoSerializer  
from .models import User

from dateutil.relativedelta import relativedelta



class UserSerializer(serializers.ModelSerializer):
    email = EmailSerializer()
    cpf = CpfSerializer()
    endereco = EnderecoSerializer()  
    class Meta:
        model = User
        fields = ('id', 'name', 'birth_date', 'cpf', 'email', 'endereco',)

    def validate_birth_date(self, value):
        today = timezone.now().date()
        age_limit_upper = today - relativedelta(years=18)
        age_limit_lower = today - relativedelta(years=100)

        if not age_limit_lower <= value <= age_limit_upper:
            raise serializers.ValidationError("A idade deve estar entre 18 e 100 anos.")
        return value

    def create(self, validated_data):
        email_data = validated_data.pop('email')
        cpf_data = validated_data.pop('cpf')
        endereco_data = validated_data.pop('endereco')  
        
        email_serializer = EmailSerializer(data=email_data)
        email_serializer.is_valid(raise_exception=True)
        email_instance = email_serializer.save()

        cpf_serializer = CpfSerializer(data=cpf_data)
        cpf_serializer.is_valid(raise_exception=True)
        cpf_instance = cpf_serializer.save()

        endereco_serializer = EnderecoSerializer(data=endereco_data)
        endereco_serializer.is_valid(raise_exception=True)
        endereco_instance = endereco_serializer.save()

        user_instance = User.objects.create(
            email=email_instance,
            cpf=cpf_instance,
            endereco=endereco_instance,
            **validated_data
        )

        return user_instance
