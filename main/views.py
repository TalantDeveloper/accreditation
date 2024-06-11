from django.shortcuts import render, redirect

from main.function import get_context
from main.models import ResultTest
from station.models import Station
from student.functions import get_group
from student.models import Student, Group


def welcome(request):
    context = get_context(request)
    return render(request, 'main/welcome.html', context)


def result_tests_view(request):
    context = get_context(request)
    if request.method == 'POST':
        print('dfsdf')
        print(request.POST.get('student'))
    return render(request, 'test/tests.html', context)


def result_test_view(request, student_id):
    context = get_context(request)
    student = Student.objects.get(pk=student_id)
    group = get_group(request, student)

    result_test = ResultTest.objects.get(student=student) or None
    if result_test:
        context['student'] = student
        context['group'] = group
        context['result_test'] = result_test
        return redirect('main:tests')
    else:
        context['student'] = student
        context['group'] = group
    return render(request, 'test/test.html', context)


def exam_view(request):
    context = get_context(request)
    if request.method == 'POST':
        student = Student.objects.get(id=request.POST.get('student'))
        station = Station.objects.get(id=request.POST.get('station'))
        context['student'] = student
        context['station'] = station
        return render(request, 'main/exam.html', context)
    return render(request, 'main/exam.html', context)
