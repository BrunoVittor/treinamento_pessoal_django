from django.db import models


# Create your models here.
class Contatos(models.Model):
  nome = models.CharField(
    max_length=200,
    blank=False,
    null=False
  )

  email = models.EmailField(
    max_length=200,
    blank=False,
    null=False
  )

  endereco = models.CharField(
    max_length=200,
    blank=False,
    null=False
  )

  telefone = models.CharField(
    max_length=200,
    blank=False,
    null=False
  )
