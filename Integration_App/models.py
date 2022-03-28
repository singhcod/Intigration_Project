from django.db import models

# Create your models here.
class Student(models.Model):
    student_rall = models.IntegerField()
    student_name = models.CharField(max_length=40)
    student_class = models.CharField(max_length=40)
    student_section = models.CharField(max_length=20)
    student_marks = models.FloatField()

    def __str__(self):
        return self.student_name

