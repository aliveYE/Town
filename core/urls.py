from django.urls import path
from . import views

urlpatterns = [
    path('', views.loader, name='loader'),
    path('home/', views.home, name='home'),
    path('lessons/', views.lessons, name='lessons'),
    path('students/', views.students, name='students'),
    path('student/<int:id>/', views.student_profile, name='student_profile'),
    path('add-student/', views.add_student, name='add_student'),
    path('grade/', views.grade_dashboard, name='grade_dashboard'),
]