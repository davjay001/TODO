from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TasksModel(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title 

