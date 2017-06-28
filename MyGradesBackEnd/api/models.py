from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models

class Semester(models.Model):
    season = models.CharField(max_length=100)
    year = models.IntegerField(null=True)

    def __str__(self):
        return self.season + " " + str(self.year)

class School(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ('user',)



class Course(models.Model):
    title = models.CharField(max_length=50)
    course_number = models.CharField(max_length=50, blank=True, null=True)
    professor = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_in_course')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    # assignments = models.ManyToManyField(Assignment, blank=True, null=True, related_name="course_of_assignment")

    def __str__(self):
        return str(self.title)


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    points_possible = models.DecimalField(max_digits=9, decimal_places=2)
    points_received = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_assignments")

    def __str__(self):
        return str(self.title)




@receiver(post_save, sender=User)
def create_student_instance(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_student_instance(sender, instance, **kwargs):
    instance.student.save()









