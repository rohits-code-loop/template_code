from django.db import models
# Create your models here.
class content(models.Model):
	text_content	= models.CharField(max_length = 1000)
	content_type 	= models.CharField(max_length = 20)
	


	

