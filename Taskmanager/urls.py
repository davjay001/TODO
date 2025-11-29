from django.urls import path
from .views import *

urlpatterns = [
    path('create-task',TaskListCreateview.as_view(), name= 'create-task' ),
    path('<int:pk>/',TaskDetailView.as_view(),name='task-detail')
]   