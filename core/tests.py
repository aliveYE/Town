

# Create your tests here.
from django.db import models

class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.subject


class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    total_grade = models.IntegerField()
    status = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='students/', blank=True)

    def __str__(self):
        return self.name
