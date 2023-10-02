from django.db import models

from email_model.models import Email
from cpf_model.models import CPF 
from endereco_model.models import Endereco  


class User(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    cpf = models.ForeignKey(CPF, on_delete=models.CASCADE)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, related_name='user', null=True, blank=True)


    def __str__(self):
        return self.name
    
