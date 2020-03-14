from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Registration(models.Model):
	fullname = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	contact = models.IntegerField()
	password1 = models.CharField(max_length=20)
	password2 = models.CharField(max_length=20)



class Employee(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)

	class Meta:
		db_table = 'student'


