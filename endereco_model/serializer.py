from rest_framework import serializers
from .models import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    def validate_cep(self, value):
        if len(value) != 8 or not value.isdigit():
            raise serializers.ValidationError("CEP inválido. Deve conter 8 dígitos.")
        return value

    class Meta:
        model = Endereco
        fields = ('id', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado')
