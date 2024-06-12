from .models import *
from student.models import *
from station.models import *

from station.function import *


def get_context(request):
    students = Student.objects.all()
    groups = Group.objects.all()
    stations = Station.objects.all()

    exams = Exam.objects.all()
    result_tests = ResultTest.objects.all()
    generals = General.objects.all()

    context = {
        'students': students,
        'groups': groups,
        'stations': stations,
        'exams': exams,
        'result_tests': result_tests,
        'generals': generals,
    }
    return context


def get_exam(student):
    exams = Exam.objects.all()
    for exam in exams:
        if exam.student.id == student.id:
            return exam
    return None


def get_result_test(student):
    result_tests = ResultTest.objects.all()
    for result_test in result_tests:
        if result_test.student.id == student.id:
            return result_test
    return None


def get_general(student):
    generals = General.objects.all()
    for general in generals:
        if general.student.id == student.id:
            return general

    return None
