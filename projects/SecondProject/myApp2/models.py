from django.db import models


class Student(models.Model):
    branches = [('cse','CSE'),
                ('ece','ECE'),
                ('it','IT'),
                ('eee','EEE')]
    language_choices = (
        ('T', 'Telugu'),
        ('E', 'English'),
        ('H', "Hindi"))
    stuid = models.CharField(max_length=10)
    stuName = models.CharField(max_length=50)
    branch = models.CharField(max_length=50,choices=branches)
    age = models.IntegerField()
    language = models.CharField(max_length=1, choices=language_choices, blank=True, null=True)

    def __str__(self):
        return self.stuName+self.stuid+self.branch