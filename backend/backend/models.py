from django.conf import settings
from django.db import models
from django.utils import timezone

class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)

class Teacher(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)

class Subject(models.Model):
    name = models.CharField(max_length=250)
    teacher = models.ForeignKey(Teacher, models.CASCADE, related_name='subjects')

class Hours(models.Model):
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    hour = models.TimeField()
    subject = models.ForeignKey(Subject, models.CASCADE, related_name='hours')

class Enrolled(models.Model):
    subject = models.ForeignKey(Subject, models.CASCADE, related_name='enrollments')
    student = models.ForeignKey(Student, models.CASCADE, related_name='enrollments')
    period = models.IntegerField()
    class Meta:
        unique_together = ('subject', 'student','period')
class Assistant(models.Model):
    enrolled = models.ForeignKey(Enrolled, models.CASCADE, related_name='assistants')
    assisted = models.BooleanField()
    hour =models.ForeignKey(Hours,models.CASCADE)
    date = models.DateField()
