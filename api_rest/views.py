from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Tasks
from .serializers import UserSerializer, TasksSerializer

import json

# Aqui vai ficar o CRUD do App.
@api_view(["GET","POST","PUT","DELETE"])
def taskManager(request): #esse é o método para o crud das tasks

    #Esse método vai ser responsavel por pegar todas as listas e entregar ao front
    if request.method == "GET":
        try: 
            tasks = Tasks.objects.all()
            serializer = TasksSerializer(tasks, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    #Esse aqui é o método responsável por criar uma nova tarefa
    if request.method == "POST":
        try: 
            new_task = request.data
            serializer = TasksSerializer(data=new_task)

            if serializer.is_valid():
                serializer.save() #Se o serializer for valido ele vai salvar o item todo
                return Response(serializer.data, status=status.HTTP_201_CREATED) #Retorna o objeto e o 201
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) #Se der ruim ele retorna o erro
        

    #Esse método é responsável por deletar as tasks do banco
    if request.method == "DELETE":
        id = request.data['task_id']
        try:
            task_to_delete = Tasks.objects.get(pk=id)
            task_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


#Esse GET vai trazer os detalhes de um item da lista em específico
@api_view(["GET", "PUT"])
def taskDetail(request, id):

    # Obtém a tarefa com o ID fornecido
    task = Tasks.objects.get(pk=id)

    if request.method == "GET":
        try:
            # Serializa os detalhes da tarefa encontrada
            serializer = TasksSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(["GET","POST","DELETE"])
def userManager(request): #esse é o método para o crud das tasks

    #Esse método vai ser responsavel por pegar os users
    if request.method == "GET":
        try: 
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    #Esse aqui é o método responsável por criar um user
    if request.method == "POST":
        try: 
            new_user = request.data
            serializer = UserSerializer(data=new_user)

            if serializer.is_valid():
                serializer.save() #Se o serializer for valido ele vai salvar o item todo
                return Response(serializer.data, status=status.HTTP_201_CREATED) #Retorna o objeto e o 201
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) #Se der ruim ele retorna o erro
        

    #Esse método é responsável por deletar as tasks do banco
    if request.method == "DELETE":
        id = request.data['task_id']
        try:
            user_to_delete = User.objects.get(pk=id)
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)