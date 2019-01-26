from django.db import models

# Create your models here.
class ProfilePhotos(models.Model):
	url = models.ImageField()	
