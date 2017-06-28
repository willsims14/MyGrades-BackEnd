from django.shortcuts import render
from rest_framework import viewsets
from MyGradesBackEnd.api.models import Course, Student, Semester, Assignment, School
from MyGradesBackEnd.api.serializers import CourseSerializer, StudentSerializer, SemesterSerializer, UserSerializer, AssignmentSerializer, SchoolSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response




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

    def perform_create(self, serializer):
        student = Student.objects.get(user=self.request.user.id)
        serializer.save(student=student)

class CourseDetail(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAssignmentsList(APIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def get(self, request):
        course_pk = request.query_params.get('course_pk', None)

        if course_pk is not None:
            assignments = Assignment.objects.filter(course=course_pk)
            serializer = AssignmentSerializer(assignments, context={'request': request}, many=True)
        return Response(serializer.data)



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




######################################################
####################  School Views  ##################
######################################################
class SchoolList(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolDetail(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer