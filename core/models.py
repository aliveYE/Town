
from PIL import Image
# Create your models here.
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            img = Image.open(self.photo.path)

            width, height = img.size
            min_side = min(width, height)

            # Center crop
            left = (width - min_side) / 2
            top = (height - min_side) / 2
            right = (width + min_side) / 2
            bottom = (height + min_side) / 2

            img = img.crop((left, top, right, bottom))

            # Resize to 300x300
            img = img.resize((300, 300), Image.LANCZOS)

            img.save(self.photo.path)

    def __str__(self):
        return self.name

class TestResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    max_score = models.IntegerField(default=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.name} - {self.date}"
