from django.db import models

# Create your models here.

class Emp(models.Model):
	"""docstring for """
	empid=models.CharField(max_length=10)
	empName=models.CharField(max_length=50)
	empDesig=models.CharField(max_length=50)
	salary=models.FloatField()

	def __str__(self):
		return self.empid+" "+self.empName
