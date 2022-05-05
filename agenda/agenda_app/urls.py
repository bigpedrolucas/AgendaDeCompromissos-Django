from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaCompromissos, name='comp-list'),
    path('compromisso/<int:id>', views.compromissoView, name='comp-view'),
    path('novocompromisso/', views.novoCompromisso, name='new-comp'),
    path('editar/<int:id>', views.editarCompromisso, name='edit-comp'),
    path('excluir/<int:id>', views.excluirCompromisso, name='del-comp'),
]
