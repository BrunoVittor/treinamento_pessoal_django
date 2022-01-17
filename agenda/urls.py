from agenda.views import IndexTemplateView, AgendaListView, ContatoCreateView, ContatoUpdateView, ContatoDeleteView
from django.urls import path

urlpatterns = [
  path('', IndexTemplateView.as_view(), name='index'),

  path('lista', AgendaListView.as_view(), name='contatos'),

  path('lista/criar', ContatoCreateView.as_view(), name='criar'),

  path('lista/editar/<pk>', ContatoUpdateView.as_view(), name='editar'),

  path('lista/delete/<pk>', ContatoDeleteView.as_view(), name='deletar')
]
