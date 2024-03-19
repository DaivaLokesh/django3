from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,blank=False)
    course=models.CharField(max_length=100,blank=False)
    fees=models.CharField(max_length=100,blank=False)

    class Meta:
        db_table='student'