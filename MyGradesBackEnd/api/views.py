from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token


# Class Based View
from rest_framework.views import APIView
from rest_framework.response import Response
# Method Based View
from rest_framework.decorators import api_view
from rest_framework import status

from django.contrib.auth.models import User

from MyGradesBackEnd.api.models import Course, Student, Semester, Assignment, School
from MyGradesBackEnd.api.serializers import CourseSerializer, StudentSerializer, SemesterSerializer, UserSerializer, AssignmentSerializer, SchoolSerializer

import json

@csrf_exempt
def register_user(request):
    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'],
                    first_name=req_body['first_name'],
                    last_name=req_body['last_name'])

    # Commit the user to the database by saving it
    new_user.save()
    token = Token.objects.create(user=new_user)
    data = json.dumps({'token':token.key, 'pk':new_user.id})

    return HttpResponse(data, content_type='application/json')


######################################################
###################  Course Views  ###################
######################################################
class CourseList(viewsets.ModelViewSet):
    # Gets all courses for current user
    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer
    ordering_fields = ('id',)

    def get_queryset(self):
        queryset = Course.objects.all().order_by('-id')
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(student__user__username=username)
        return queryset

    # Overrides perform_create to attach the current student to the newly created course
    def perform_create(self, serializer):
        student = Student.objects.get(user=self.request.user.id)
        # semester = Semester.objects.get(pk=self.req_body['semester'])
        serializer.save(student=student)

class CourseDetail(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer

class CourseAssignmentsList(APIView):
    queryset = Assignment.objects.all().order_by('-id')
    serializer_class = AssignmentSerializer

    def get_object(self, pk):
        try:
            return Assignment.objects.filter(course=pk)
        except Assignment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        assignments = self.get_object(pk)
        serializer = AssignmentSerializer(assignments, context={'request': request}, many=True)
        return Response(serializer.data)




######################################################
###################  Student Views  ##################
######################################################
class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer

class StudentDetail(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer

# Retrieves student via authentication token
class GetStudentByTokenView(APIView):
    def get(self, request, token, format=None):
        try:
            token_obj = Token.objects.get(pk=token)
            user = User.objects.get(pk=token_obj.user.id)
            serializer = StudentSerializer(user.student, context={'request': request})
            return Response(serializer.data)
        except Token.DoesNotExist:
            raise Http404


######################################################
###################  Semester Views  #################
######################################################
class SemesterList(viewsets.ModelViewSet):
    queryset = Semester.objects.all().order_by('-id')
    serializer_class = SemesterSerializer





class SemesterDetail(viewsets.ModelViewSet):
    queryset = Semester.objects.all().order_by('-id')
    serializer_class = SemesterSerializer



######################################################
###################  User Views  #####################
######################################################
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

class UserDetail(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


######################################################
################  Assignment Views  ##################
######################################################
class AssignmentList(viewsets.ModelViewSet):
    queryset = Assignment.objects.all().order_by('-id')
    serializer_class = AssignmentSerializer

class AssignmentDetail(viewsets.ModelViewSet):
    queryset = Assignment.objects.all().order_by('-id')
    serializer_class = AssignmentSerializer


######################################################
####################  School Views  ##################
######################################################
class SchoolList(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('-id')
    serializer_class = SchoolSerializer

class SchoolDetail(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('-id')
    serializer_class = SchoolSerializer