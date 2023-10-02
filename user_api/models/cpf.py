from django.db import models


class CPF(models.Model):
    cpf_number = models.CharField(max_length=11, unique=True)

    def is_valid_cpf(self, cpf):
        """Verifica se um CPF é válido."""
        cpf = ''.join(c for c in cpf if c.isdigit())
        
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        
        # Calcula o primeiro dígito verificador
        total = sum(int(cpf[i]) * (10 - i) for i in range(9)) % 11
        digit1 = 0 if total < 2 else 11 - total

        # Calcula o segundo dígito verificador
        total = sum(int(cpf[i]) * (11 - i) for i in range(10)) % 11
        digit2 = 0 if total < 2 else 11 - total

        # Verifica se os dígitos verificadores são válidos
        return cpf[-2:] == f'{digit1}{digit2}'

    def save(self, *args, **kwargs):
        if not self.is_valid_cpf(self.cpf_number):
            raise ValueError("CPF inválido")
        super(CPF, self).save(*args, **kwargs)

    def __str__(self):
        return self.cpf_number

