from rest_framework import serializers
from django.contrib.auth.models import User
from MyGradesBackEnd.api.models import Course, Student, Semester, Assignment


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        exclude = ()


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        exclude = ('url','user',)


class SemesterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Semester
        exclude = ('url',)


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        exclude = ('first_name', 'last_name', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'user_permissions', 'groups', 'password')






class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        exclude = ()



