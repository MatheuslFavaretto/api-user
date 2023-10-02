import requests
from rest_framework import viewsets
from user_api.models.endereco import Endereco
from user_api.serializers.endereco import EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def perform_create(self, serializer):
        cep = serializer.validated_data['cep']
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            # Salva os dados do ViaCEP no banco de dados
            endereco_obj = serializer.save(
                logradouro=data.get('logradouro', ''),
                complemento=data.get('complemento', ''),
                bairro=data.get('bairro', ''),
                cidade=data.get('localidade', ''),
                estado=data.get('uf', '')
            )
        else:
            raise serializer.ValidationError({'error': 'CEP não encontrado no ViaCEP'})
        
        return endereco_obj
