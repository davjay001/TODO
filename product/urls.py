from django.urls import path
from .views import  create_school,create_student,hello_world,student_list_create

urlpatterns = [
    # path('products/', product_list, name='product-list'),
    path('schools/', create_school,name='create-school'),
    path('students/', create_student, name='create-student'),
    path('hello/', hello_world,name="hello-world"),
    path('list', student_list_create,name='student_list_create')
]