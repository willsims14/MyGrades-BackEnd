"""
bangazon factory to create sample data to seed a database using Faker in lieu of using 
fixtures
"""

import factory
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from MyGradesBackEnd.api.models import Semester, School, Course, Student



class UserFactory(factory.django.DjangoModelFactory):


    class Meta:
        model = User

    password = factory.Faker('uuid4')
    last_login = timezone.now()
    is_superuser = "0"
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    is_staff = "0"
    is_active = "1"
    date_joined = timezone.now()
    username = factory.Faker('uuid4')

class Semester1Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = Semester

    season = 'Fall'
    year = 2017

class Semester2Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = Semester

    season = 'Spring'
    year = 2017


class SchoolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = School

    name = "University of Tennessee"
    state = "TN"
    city = "Knoxville"


# class CourseFactory(factory.django.DjangoModelFactory):
#     student = Student.objects.get(pk=1)
#     semester = Semester.objects.get(pk=1)
#     class Meta:
#         model = Course

#     title = "Finite Mathematics"
#     course_number = "MATH 123"
#     professor = "Jim Plank"
#     description = "Boring class with lots of homework"
#     student = student
#     semester = semester
