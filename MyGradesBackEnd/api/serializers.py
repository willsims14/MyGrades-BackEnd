from rest_framework import serializers
from django.contrib.auth.models import User
from MyGradesBackEnd.api.models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(read_only=True)
    class Meta:
        model = Course
        exclude = ()