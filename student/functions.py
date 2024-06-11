from .models import Student, Group
from main.function import get_context, get_exam, get_result_test, get_general


def get_students(request):
    students = Student.objects.all()
    return students


def get_groups(request):
    groups = Group.objects.all()
    students = get_students(request)
    return {'groups': groups, 'students': students}


def get_group(request, student):
    groups = Group.objects.all()
    for group in groups:
        if student in group.students.all():
            return group
    return None


def get_student(request, student):
    context = get_context(request)
    group = get_group(request, student)
    exam = get_exam(student)
    result_test = get_result_test(student)
    general = get_general(student)

    context['group'] = group
    context['exam'] = exam
    context['result_test'] = result_test
    context['general'] = general
    return context




