from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class user(models.Model):
	usrID 			= 	models.CharField(max_length=30, primary_key = True )
	name 			= 	models.CharField(max_length=30,blank = False )
	age 			= 	models.CharField(max_length=10,blank = False )
	email 			= 	models.CharField(max_length =30 ,unique = True )
	password 		= 	models.CharField(max_length = 64 )
	#active 			= 	models.CharField(max_length=2 , blank = True)
