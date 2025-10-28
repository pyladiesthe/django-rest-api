from django.urls import path
from .views import lista_tarefas, cria_tarefa, atualiza_tarefa, deleta_tarefa, lista_concluidas

urlpatterns = [
	path('', lista_tarefas, name='lista_tarefas'),
	path('criar/', cria_tarefa, name='cria_tarefa'),
	path('atualiza/<int:pk>/', atualiza_tarefa, name='atualiza_tarefa'),
	path('deleta/<int:pk>/', deleta_tarefa, name='deleta_tarefa'),
	path('concluidas/', lista_concluidas, name='lista_concluidas')
]

