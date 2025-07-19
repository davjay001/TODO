from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,School,Student
from .serializers import SchoolSerializer,StudentSerializer
from rest_framework import status

# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_product(request):
#     serializer= ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=201)
#     return Response(serializer.errors,status=400)

@api_view(['POST'])
def create_school(request):
    serializer = SchoolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data":serializer.data} ,status=201)
        
        
    return Response({'error' : serializer.errors})


@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data":serializer.data}, status=201)

def school_list():
    pass

def student_list():
    pass

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET','POST'])
def student_list_create(request):
    if request.method == 'GET':
        students  = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'message':'Student sucessfully created'} , status = 201)
        return Response({'error':serializer.errors})

        
    