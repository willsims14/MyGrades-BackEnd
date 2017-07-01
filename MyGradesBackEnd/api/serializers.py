from rest_framework import serializers
from django.contrib.auth.models import User
from MyGradesBackEnd.api.models import Course, Student, Semester, Assignment, School


class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        exclude = ()

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    # course_assignments = serializers.StringRelatedField(many=True)
    assignments = AssignmentSerializer(many=True)
    current_grade = serializers.SerializerMethodField()
    semester = serializers.CharField()
    id = serializers.CharField()

    def get_current_grade(self, obj):
        return obj.calculate_grade()

    class Meta:
        model = Course
        exclude = ('student',)


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    username = serializers.CharField(source="user.username")
    class Meta:
        model = Student
        exclude = ('user',)


class SemesterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Semester
        exclude = ('url',)

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        exclude = ('url',)


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        exclude = ('first_name', 'last_name', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'user_permissions', 'groups', 'password')










