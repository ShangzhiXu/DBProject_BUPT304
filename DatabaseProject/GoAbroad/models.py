from django.db import models


class Student(models.Model):
    student_ID = models.CharField(max_length=200, primary_key=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    GPA = models.FloatField(null=True, blank=True)
    Rank = models.CharField(max_length=200, null=True, blank=True)
    scholarship = models.CharField(max_length=200, null=True, blank=True)
    Hand_in_date = models.DateField(null=True, blank=True)
    get_offer_date = models.DateField(null=True, blank=True)
    major = models.ForeignKey("Major", null=True, blank=True, default='', on_delete=models.CASCADE)
    program_name = models.ForeignKey("Program", null=True, blank=True, default='', on_delete=models.CASCADE)
    teacher_name = models.ForeignKey("Teacher", null=True, blank=True, default='', on_delete=models.CASCADE)
    school_name = models.ForeignKey("School", null=True, blank=True, default='', on_delete=models.CASCADE)
    practice = models.ForeignKey("Practice", null=True, blank=True, default='', on_delete=models.CASCADE)
    other = models.CharField(max_length=10000, null=True, blank=True)


class School(models.Model):
    school_name = models.CharField(max_length=200, primary_key=True)
    qs_rank = models.IntegerField(null=True, blank=True)
    enrollment = models.IntegerField(null=True, blank=True)
    final_number = models.IntegerField(null=True, blank=True)
    enrollment_for_bupt = models.IntegerField(null=True, blank=True)


class English(models.Model):
    test_name = models.CharField(max_length=200, primary_key=True)
    grade = models.FloatField(null=True, blank=True)


class Competition(models.Model):
    competition_name = models.CharField(max_length=200, primary_key=True)
    prize = models.CharField(max_length=200, null=True, blank=True)
    level = models.CharField(max_length=200, null=True, blank=True)


class in_Competition(models.Model):
    competition_name = models.CharField(max_length=200, null=True, blank=True)
    student_ID = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.competition_name, self.student_ID


class in_English(models.Model):
    test_name = models.CharField(max_length=200, null=True, blank=True)
    student_ID = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.test_name, self.student_ID


class Practice(models.Model):
    company_name = models.CharField(max_length=200, primary_key=True)
    leader_name = models.CharField(max_length=200, null=True, blank=True)
    work_time = models.CharField(max_length=200, null=True, blank=True)
    payment = models.FloatField(null=True, blank=True)
    house = models.CharField(max_length=200, null=True, blank=True)
    rent = models.FloatField(null=True, blank=True)


class in_Practice(models.Model):
    company_name = models.CharField(max_length=200, null=True, blank=True)
    student_ID = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name, self.student_ID


class Major(models.Model):
    major = models.CharField(max_length=200, primary_key=True)
    short = models.CharField(max_length=200, null=True, blank=True)


class Application(models.Model):
    school_name = models.CharField(max_length=200, null=True, blank=True)
    student_ID = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name, self.student_ID


class Agent(models.Model):
    agent_name = models.CharField(max_length=200, primary_key=True)
    cost = models.FloatField(null=True, blank=True)
    evaluate = models.CharField(max_length=200, null=True, blank=True)


class choice_agent(models.Model):
    agent_name = models.CharField(max_length=200)
    student_ID = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name, self.student_ID


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200, primary_key=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)


class Program(models.Model):
    program_name = models.CharField(max_length=200, primary_key=True)
    nation = models.CharField(max_length=200, null=True, blank=True)
    awards = models.CharField(max_length=200, null=True, blank=True)  # 奖学金情况
    plan = models.IntegerField(null=True, blank=True)  # 招生人数
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
