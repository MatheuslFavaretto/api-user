from rest_framework import serializers

from .models import CPF


class CpfSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPF
        fields = ('cpf_number', )  # Inclua outros campos conforme necessário
