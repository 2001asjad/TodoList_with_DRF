from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer

from app.models import Todo

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Todo-list/',
		'Detail View':'/Todo-detail/<str:pk>/',
		'Create':'/Todo-create/',
		'Update':'/Todo-update/<str:pk>/',
		'Delete':'/Todo-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def TodoList(request):
	Todos = Todo.objects.all().order_by('-id')
	serializer = TodoSerializer(Todos, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def TodoDetail(request, pk):
	Todos = Todo.objects.get(id=pk)
	serializer = TodoSerializer(Todos, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def TodoCreate(request):
	serializer = TodoSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def TodoUpdate(request, pk):
	Todo = Todo.objects.get(id=pk)
	serializer = TodoSerializer(instance=Todo, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def TodoDelete(request, pk):
	Todo = Todo.objects.get(id=pk)
	Todo.delete()

	return Response('Item succsesfully delete!')
