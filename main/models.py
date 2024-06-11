from django.db import models
from student.models import Student, Group
from station.models import Station, Title


class Result(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.ForeignKey(Title, verbose_name="Title", on_delete=models.SET_NULL, null=True, blank=True)
    station = models.ForeignKey(Station, verbose_name="Station", on_delete=models.SET_NULL, null=True, blank=True)
    result = models.BooleanField(verbose_name="Result", default=False)

    def __str__(self):
        return f"{self.title}: {self.station}"


class Exam(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name="Group", on_delete=models.SET_NULL, null=True, blank=True)
    station = models.ForeignKey(Station, verbose_name="Station", on_delete=models.SET_NULL, null=True, blank=True)
    result = models.FloatField(verbose_name="Result", default=0.0)

    def __str__(self):
        return f"{self.result} %"


class ResultTest(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name="Group", on_delete=models.SET_NULL, null=True, blank=True)
    result = models.FloatField(verbose_name="Result", default=0.0)

    def __str__(self):
        return f"{self.result}"


class General(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name="Group", on_delete=models.SET_NULL, null=True, blank=True)
    result_test = models.ForeignKey(ResultTest, verbose_name="Result", on_delete=models.SET_NULL, null=True, blank=True)
    exam = models.ForeignKey(Exam, verbose_name="Exam", on_delete=models.SET_NULL, null=True, blank=True)
    result_sum = models.FloatField(verbose_name="ResultSum", default=0.0)

    def __str__(self):
        return f"{self.id} - {self.student}"
