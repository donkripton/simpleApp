from django.db import models

# Create your models here.
class EmployeeInfo(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	email = models.CharField(max_length=30)

	def __str__(self):
		return self.email