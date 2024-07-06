from django.shortcuts import render
from student.models import Student, Group
from station.models import Station, Title
from main.models import Result, Exam, ResultTest, General
from .serializers import StationSerializer, StudentSerializer, GroupSerializer, TitleSerializer, ResultSerializer, \
    ResultTestSerializer, ExamSerializer, GeneralSerializer

from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
