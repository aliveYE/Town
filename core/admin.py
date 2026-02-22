from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Lesson, TestResult, Attendance 

admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(TestResult)
admin.site.register(Attendance)


