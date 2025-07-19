from rest_framework import serializers
from .models import School,Student


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'first_name', 'last_name', 'age', 'enrolled', 'full_name']
    
#     def get_full_name(self, obj):
#         return f"{obj.first_name} {obj.last_name}"

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
    
