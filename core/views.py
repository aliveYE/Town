from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .models import Student, Lesson, Attendance
from .forms import StudentForm


# ======================
# LOADER
# ======================
def loader(request):
    return render(request, 'loader.html')


# ======================
# HOME
# ======================
def home(request):
    return render(request, 'home.html')


# ======================
# LESSONS
# ======================
def lessons(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons.html', {'lessons': lessons})


# ======================
# STUDENTS LIST
# ======================
def students(request):
    query = request.GET.get('q')
    students = Student.objects.all().order_by('-total_grade')

    if query:
        students = students.filter(name__icontains=query)

    return render(request, 'students.html', {
        'students': students
    })


# ======================
# STUDENT PROFILE
# ======================
def student_profile(request, id):
    student = get_object_or_404(Student, id=id)
    results = student.results.all()
    attendance = Attendance.objects.filter(student=student)

    return render(request, 'student_profile.html', {
        'student': student,
        'results': results,
        'attendance': attendance
    })


# ======================
# ADD STUDENT (REAL WORKING FORM)
# ======================
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


# ======================
# DASHBOARD
# ======================
def grade_dashboard(request):
    student_count = Student.objects.count()
    lesson_count = Lesson.objects.count()
    attendance_percent = 94  # Static for now

    return render(request, 'grade_dashboard.html', {
        'student_count': student_count,
        'lesson_count': lesson_count,
        'attendance_percent': attendance_percent
    })


# ======================
# LOGIN
# ======================
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')