from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    courses = models.ManyToManyField(Course, related_name='students')
