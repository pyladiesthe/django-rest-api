from django.db import models

class Tarefa(models.Model):

	status_choice = {
		'P': 'PENDENTE',
		'A': 'ANDAMENTO',
		'C': 'CONCLUIDO'
	}

	titulo = models.CharField(max_length=200)
	descricao = models.TextField(blank=True)
	status = models.CharField(max_length=1, choices=status_choice, default='P')
	data_criacao = models.DateField(auto_now=True)

	def __str__(self):
		return self.titulo

