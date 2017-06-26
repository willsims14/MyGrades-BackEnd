from django.shortcuts import render
from rest_framework import viewsets
from MyGradesBackEnd.api.models import Course
from MyGradesBackEnd.api.serializers import CourseSerializer


# Create your views here.
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