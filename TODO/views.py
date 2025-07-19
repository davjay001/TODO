from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile, Tasks
from.serializers import ProfileSerializer, TasksSerializer

@api_view(['POST'])
def signup(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Signed up sucessfully'}, status=201)
    
    return Response({"error": serializer.errors})

@api_view(['POST'])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        profile = Profile.objects.get(email=email, password=password)
        serializer = ProfileSerializer(profile)
        return Response({'message': 'Signed in successfully'}, status=200)
    except Profile.DoesNotExist:
        return Response({'error': 'Invalid email or password'}, status=400)
    
@api_view(['GET','POST','PUT'])
def task_list_create(request,id):
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Task created'}, status=201)
        return Response({"error": serializer.errors})
    
    elif request.method == 'PUT':
        tasks = Tasks.objects.get(id=id)
        serializer = TasksSerializer(tasks,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Updated sucessfully"}, status=201)
        return Response({"errors":serializer.errors})


# @api_view(['PUT'])
# def update_task(request,id):
#     tasks = Tasks.objects.get(id=id)
