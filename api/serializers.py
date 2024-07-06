from student.models import Student, Group
from station.models import Station, Title
from main.models import Result, Exam, ResultTest, General

from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'title']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'get_students']


class TitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Title
        fields = ('id', 'url', 'title')


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'url', 'name', 'get_titles')


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ResultTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResultTest
        fields = '__all__'


class GeneralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = General
        fields = '__all__'
