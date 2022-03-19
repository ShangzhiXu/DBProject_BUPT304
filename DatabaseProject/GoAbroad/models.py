
from django.db import models


class Student(models.Model):
    student_ID = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    GPA = models.FloatField()
    Rank =  models.CharField(max_length=200)
    scholarship = models.CharField(max_length=200)
    Hand_in_date = models.DateField()
    get_offer_date = models.DateField()

    def __str__(self):
        return self.student_ID



class School(models.Model):
    school_Name = models.CharField(max_length=200)
    qs_rank= models.IntegerField()
    enrollment = models.IntegerField()
    enrollment_for_bupt = models.IntegerField()

    def __str__(self):
        return self.school_Name
