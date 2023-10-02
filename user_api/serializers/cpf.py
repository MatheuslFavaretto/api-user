from rest_framework import serializers

from user_api.models.cpf import CPF


class CpfSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPF
        fields = ('id', 'cpf_number') 