
from django.db import models


class Student(models.Model):
    student_ID = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    GPA = models.FloatField()
    Rank =  models.CharField(max_length=200)
    scholarship = models.CharField(max_length=200)
    Hand_in_date = models.DateField()
    get_offer_date = models.DateField()
    major = models.CharField(max_length=200)
    program_name = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200)
    other = models.CharField(max_length=10000)


    def __str__(self):
        return self.student_ID



class School(models.Model):
    school_name = models.CharField(max_length=200)
    qs_rank= models.IntegerField()
    enrollment = models.IntegerField()
    final_number = models.IntegerField()
    enrollment_for_bupt = models.IntegerField()

    def __str__(self):
        return self.school_name

class English(models.Model):
    test_name = models.CharField(max_length=200)
    grade = models.FloatField()

    def __str__(self):
        return self.test_name

class Competition(models.Model):
    competition_name = models.CharField(max_length=200)
    prize = models.CharField(max_length=200)
    level = models.CharField(max_length=200)

    def __str__(self):
        return self.competition_name

class in_Competition(models.Model):
    competition_name = models.CharField(max_length=200)
    student_ID = models.CharField(max_length=200)

    def __str__(self):
        return self.competition_name,self.student_ID

class in_English(models.Model):
    test_name = models.CharField(max_length=200)
    student_ID = models.CharField(max_length=200)

    def __str__(self):
        return self.test_name,self.student_ID

class Practice(models.Model):
    company_name = models.CharField(max_length=200)
    leader_name = models.CharField(max_length=200)
    work_time = models.CharField(max_length=200)
    payment = models.FloatField()
    house = models.CharField(max_length=200)
    rent = models.FloatField()

    def __str__(self):
        return self.company_name

class in_Practice(models.Model):
    company_name = models.CharField(max_length=200)
    student_ID = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name,self.student_ID

class Major(models.Model):
    major = models.CharField(max_length=200)
    short = models.CharField(max_length=200)

    def __str__(self):
        return self.major

class Application(models.Model):
    school_name = models.CharField(max_length=200)
    student_ID = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name,self.student_ID

class Agent(models.Model):
    agent_name = models.CharField(max_length=200)
    cost = models.FloatField()
    evaluate = models.CharField(max_length=200)

    def __str__(self):
        return self.agent_name

class choice_agent():
    agent_name = models.CharField(max_length=200)
    student_ID = models.CharField(max_length=200)

    def __str__(self):
        return self.agent_name,self.student_ID

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)

    def __str__(self):
        return self.teacher_name

class Program(models.Model):
    program_name = models.CharField(max_length=200)
    nation = models.CharField(max_length=200)
    awards = models.CharField(max_length=200)#奖学金情况
    plan = models.IntegerField()#招生人数
    teacher_name = models.CharField(max_length=200)

    def __str__(self):
        return self.program_name
