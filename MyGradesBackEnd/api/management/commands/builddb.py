"""
djangazon api custom command to build database
"""

from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import makemigrations
from MyGradesBackEnd.api.factories import UserFactory, Semester1Factory, Semester2Factory, SchoolFactory


class Command(BaseCommand):

    
    def handle(self, *args, **options):
        # management.call_command('makemigrations', 'api')
        # management.call_command('migrate')
        UserFactory.create_batch(size=50)
        Semester1Factory.create_batch(size=1)
        Semester2Factory.create_batch(size=1)
        SchoolFactory.create_batch(size=1)
        # CourseFactory.create_batch(size=1)
        management.call_command('runserver')


