from django.db import models


# Create your models here.

    

class Profile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100,default='kajan')
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_tasks = models.IntegerField(default=0)

    def __str__(self):
        return self.email

class Tasks(models.Model):
    title = models.CharField(max_length=256)
    details = models.CharField(max_length=256)
    time_scheduled = models.DateTimeField(blank=True,null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='task')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.profile.email}"
    
