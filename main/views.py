from django.shortcuts import render, redirect

from main.function import get_context, get_result_test, login_function
from main.models import ResultTest, Result, Exam, General
from station.models import Station
from student.functions import get_group
from student.models import Student, Group
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        return login_function(request)
    return render(request, 'main/login.html')


@login_required
def welcome(request):
    context = get_context(request)
    generals = context['generals']
    hour_pirsent = [student for student in generals if student.student == 100.0]
    eyti_pirsent = [student for student in generals if student.result_sum > 85 and student.result_sum < 100.0]
    six_pirsent = [student for student in generals if student.exam.result > 60 and student.exam.result < 85.1]
    pass_pirsent = [student for student in generals if student.exam.result < 60.0]

    context['hour_pirsent'] = hour_pirsent
    context['eyti_pirsent'] = eyti_pirsent
    context['six_pirsent'] = six_pirsent
    context['pass_pirsent'] = pass_pirsent
    return render(request, 'main/welcome.html', context)


@login_required
def result_tests_view(request):
    context = get_context(request)
    if request.method == 'POST':
        print('dfsdf')
        print(request.POST.get('student'))
    return render(request, 'test/tests.html', context)


# def result_test_view(request):
#     context = get_context(request)
#     students = context['students']
#     student_list = []
#     result_tests = context['result_tests']
#     for student in students:
#         result_test = ResultTest.objects.get(student=student)
#         if result_test is None:
#             student_list.append(student)
#
#     context['student_list'] = student_list
#     return render(request, 'test/test.html', context)


@login_required
def exam_view(request):
    context = get_context(request)
    if request.method == 'POST':
        student = Student.objects.get(id=request.POST.get('student'))
        station = Station.objects.get(id=request.POST.get('station'))
        context['student'] = student
        context['station'] = station
        return render(request, 'main/exam.html', context)
    return render(request, 'main/exam.html', context)


@login_required
def check_exam(request):
    context = get_context(request)
    station = Station.objects.get(id=request.POST.get('station'))
    student = Student.objects.get(id=request.POST.get('student'))
    group = get_group(request, student)
    result_test = get_result_test(student)

    if request.method == 'POST':
        k = 0
        print(request.POST.get('1'))
        for title in station.titles.all():
            result = Result.objects.create(title=title, student=student, station=station)
            if request.POST.get(str(title.id)) == 'on':
                k += 1
                result.result = True
            else:
                result.result = False
            result.save()
        result_exam = float((k/station.titles.count())*100)
        print(result_exam)
        exam = Exam.objects.create(student=student, group=group, station=station, result=result_exam)
        exam.save()

        if result_test is None:
            result_test = ResultTest.objects.create(student=student, group=group, result=0.0)
            result_test.save()
        general = General.objects.create(student=student, group=group, exam=exam, result_test=result_test)
        general.result_sum = (exam.result + result_test.result) / 2
        general.save()
        return redirect('student:groups')
    return render(request, 'main/exam.html', context)


@login_required
def result_view(request):
    context = get_context(request)
    return render(request, 'main/results.html', context)


@login_required
def result_group(request, group_id):
    group = Group.objects.get(id=group_id)
    context = get_context(request)
    results_group = General.objects.filter(group=group)
    context['results_group'] = results_group
    context['group'] = group
    return render(request, 'main/result_group.html', context)


def not_page(request):
    return render(request, 'main/login.html')


def create_student(request):
    with open('.//static/student.txt', 'r') as f:
        text = f.readlines()
        for line in text:
            group = Group.objects.create(name=line)
            group.save()
    return render(request, 'student/create.html')
