from django.db import models
from django.db.models import Count, Avg, Max

# Create your models here.
 
class Product(models.Model):
    title = models.CharField(max_length=23)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class School(models.Model):
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255,default="perm site",blank=True,null=True)



class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,default='ajayi')
    bio = models.CharField(max_length=255,null=True,blank=True)
    age = models.IntegerField(blank=True, null=True,default=17)
    school = models.ForeignKey(School,related_name="student", on_delete=models.CASCADE)

    class Meta:
        ordering = ['first_name','age']
        # unique_together = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} - {str(self.age)}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Courses(models.Model):
    name = models.CharField(max_length=100)
    students= models.ManyToManyField(Student,related_name="students")



class CustomUser(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    username= models.CharField(max_length=200)

class Profile(models.Model):
    dob = models.DateField()
    marital_status = models.CharField(max_length=20,default='single')
    user = models.OneToOneField(CustomUser,related_name='profile',on_delete=models.CASCADE)


     

class Teachers(models.Model):
    name = models.CharField(max_length=100)
    

class Subjects(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teachers,on_delete=models.CASCADE,related_name="subjects")



class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=17)
    subjects = models.ManyToManyField(Subjects,related_name="students")

    def get_status(self):
        enrollment = "Enrolled" if self.subjects.exists() else "Not Enrolled"

        return f"{self.name} (Age: {self.age}) - {enrollment}"
    
    def __str__(self):
        return f"{self.name}"
    



# _lookup
# _iexact
# _contains
