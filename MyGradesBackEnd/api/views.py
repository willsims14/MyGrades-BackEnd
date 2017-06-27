from django.shortcuts import render
from rest_framework import viewsets
from MyGradesBackEnd.api.models import Course, Student, Semester, Assignment
from MyGradesBackEnd.api.serializers import CourseSerializer, StudentSerializer, SemesterSerializer, UserSerializer, AssignmentSerializer
from django.contrib.auth.models import User


######################################################
###################  Course Views  ###################
######################################################
class CourseList(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(student__user__username=username)
        return queryset

class CourseDetail(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


######################################################
###################  Student Views  ##################
######################################################
class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


######################################################
###################  Semester Views  #################
######################################################
class SemesterList(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class SemesterDetail(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


######################################################
###################  User Views  #####################
######################################################
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


######################################################
################  Assignment Views  ##################
######################################################
class AssignmentList(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentDetail(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer








