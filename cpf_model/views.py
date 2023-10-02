from rest_framework import viewsets

from .models import CPF
from .serializer import CpfSerializer


class CpfViewSet(viewsets.ModelViewSet):
    queryset = CPF.objects.all()
    serializer_class = CpfSerializer
