from .models import Contatos
from django import forms


class CriaContatoForm(forms.ModelForm):
  class Meta:
    model = Contatos
    fields = [
      'nome',
      'email',
      'endereco',
      'telefone',
    ]
