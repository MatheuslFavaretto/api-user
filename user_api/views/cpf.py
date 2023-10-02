from rest_framework import viewsets

from user_api.models.cpf import CPF
from user_api.serializers.cpf import CpfSerializer


class CpfViewSet(viewsets.ModelViewSet):
    queryset = CPF.objects.all()
    serializer_class = CpfSerializer
