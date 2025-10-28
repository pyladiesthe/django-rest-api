from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status

from .models import Tarefa
from .serializers import TarefaSerializer


@api_view(['GET'])
def lista_tarefas(request):
	if request.method == 'GET':
		# tarefas = Tarefa.objects.all()
		tarefas = Tarefa.objects.all().order_by('status')
		tarefa_serializer = TarefaSerializer(tarefas, many=True)

		return Response(tarefa_serializer.data)


@api_view(['GET'])
def lista_concluidas(request):
	if request.method == 'GET':
		tarefas_concluidas = Tarefa.objects.filter(status='C')
		tarefa_serializer = TarefaSerializer(tarefas_concluidas, many=True)

		return Response(tarefa_serializer.data)
		

@api_view(['POST'])
def cria_tarefa(request):
	if request.method == 'POST':
		tarefa_serializer = TarefaSerializer(data=request.data)

		if tarefa_serializer.is_valid():
			tarefa_serializer.save()

			return Response(tarefa_serializer.data, status=status.HTTP_201_CREATED)

	return Response(tarefa_serializer.errors, status=status.HTTP_404_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def atualiza_tarefa(request, pk):
	try:
		tarefa = Tarefa.objects.get(pk=pk)
	except:
		return Response({"error": "Tarefa não encontrada"})


	if request.method == 'PUT' or request.method == 'PATCH':
		atualizar_parcial = True if request.method == 'PATCH' else False

		tarefa_serializer = TarefaSerializer(tarefa, data=request.data, partial=atualizar_parcial)

		if tarefa_serializer.is_valid():
			tarefa_serializer.save()

			return Response(tarefa_serializer.data, status=status.HTTP_200_OK)

		return Response(tarefa_serializer.errors, status=status.HTTP_404_BAD_REQUEST)


@api_view(['DELETE'])
def deleta_tarefa(request, pk):
	try:
		tarefa = Tarefa.objects.get(pk=pk)
	except:
		return Response({"error": "Tarefa não encontrada"})

	if request.method == 'DELETE':

		tarefa.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)
