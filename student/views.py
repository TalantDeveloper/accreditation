from django.shortcuts import render
from .functions import get_students, get_student
from .models import Student, Group
from main.function import get_context


def students_view(request):
    context = get_context(request)
    return render(request, 'student/students.html', context)


def student_view(request, student_id):
    student = Student.objects.get(id=student_id)
    context = get_student(request, student)
    context['student'] = student
    return render(request, 'student/student.html', context)


def groups_view(request):
    context = get_context(request)
    return render(request, 'student/groups.html', context)


def group_view(request, group_id):
    context = get_context(request)
    group = Group.objects.get(id=group_id)
    context['group'] = group
    return render(request, 'student/group.html', context)
