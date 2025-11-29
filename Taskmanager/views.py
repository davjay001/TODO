from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TasksModel
from .serializers import TasksSerializer
from rest_framework.permissions import IsAuthenticated

class TaskListCreateview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        auth_user = request.user
        tasks = TasksModel.objects.filter(user = auth_user)
        serializer= TasksSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message":"Added Successfully"}, status=201)
        return Response({"errors":serializer.errors})
    
class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # def get_object(self, pk, user):
    #     return get_object(TasksModel)

    def get(self, request, pk):
        try:

            tasks = TasksModel.objects.get(pk= pk,user= request.user)
        except TasksModel.DoesNotExist:
            return Response({"error":"TAsk not found or u dont have permission to view iut"})
        serializer = TasksSerializer(tasks)
        return Response(serializer.data)
    
    def put(self,request,pk):
        task = TasksModel.objects.get(pk=pk,user=request.user)
        serializer = TasksSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message":"Updated sucessfully"})
        return Response({"errors":serializer.errors})
    
    def delete(self, request, pk):
        task = TasksModel.objects.get(pk=pk,user=request.user)
        task.delete()
        return Response({"message":"Task Deleted"})

    # def put(self,request,pk):
        