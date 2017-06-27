from rest_framework import serializers
from django.contrib.auth.models import User
from MyGradesBackEnd.api.models import Course, Student, Semester


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        exclude = ()


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source="user.username")
    class Meta:
        model = Student
        exclude = ('url','user',)


class SemesterSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(source="season")
    class Meta:
        model = Semester
        exclude = ()
