from django.db import models


class Emp(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name+" "+str(self.age)

class Register(models.Model):
    # name = models.CharField(max_length=100)
    # mobileno = models.P
    # email
    pass