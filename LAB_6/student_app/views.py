from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students_list = Student.objects.all()
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')

    context = {
        'students_list': students_list,
        'form': form,
    }
    return render(request, 'student_app/students.html', context)

def courses(request):
    courses_list = Course.objects.all()
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')

    context = {
        'courses_list': courses_list,
        'form': form,
    }
    return render(request, 'student_app/courses.html', context)

def details(request, student_id):
    student = Student.objects.get(id=student_id)
    available_courses = Course.objects.exclude(students=student)

    if request.method == 'POST':
        course_id = request.POST['course']
        course = Course.objects.get(id=course_id)
        student.courses.add(course)

    context = {
        'student': student,
        'available_courses': available_courses,
    }
    return render(request, 'student_app/details.html', context)
