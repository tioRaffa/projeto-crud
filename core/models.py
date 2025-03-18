from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    name = models.CharField(("Nome"), max_length=30, blank=False, null=False)
    email = models.EmailField(("Email"), max_length=254, blank=False, null=False)
    adress = models.TextField(("Endereco"))
    phone = models.CharField(("Telefone"), max_length=13)
    