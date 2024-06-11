from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    title = models.CharField(max_length=100, verbose_name="Title", null=True, blank=True)

    def __str__(self):
        return self.full_name


class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    students = models.ManyToManyField(Student, verbose_name="Students", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_students(self):
        students = [student.full_name for student in self.students.all()]
        return students
