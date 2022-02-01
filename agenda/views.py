from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CriaContatoForm
from .models import Contatos
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


class IndexTemplateView(TemplateView):
  template_name = 'index.html'

# +++++++++++++++++++++++++++++++++++++
class AgendaListView(ListView):
  template_name = 'lista.html'
  model = Contatos
  context_object_name = 'contatos'


class ContatoCreateView(CreateView):
  template_name = 'criar.html'
  model = Contatos
  form_class = CriaContatoForm
  success_url = reverse_lazy('contatos')


class ContatoUpdateView(UpdateView):
  template_name = 'editar.html'
  model = Contatos
  fields = '__all__'
  context_object_name = 'contatos'
  success_url = reverse_lazy('contatos')


class ContatoDeleteView(DeleteView):
  template_name = 'deletar.html'
  model = Contatos
  context_object_name = 'contatos'
  success_url = reverse_lazy('contatos')
