from django.db import models
class Event(models.Model):
	name = models.CharField(max_length = 15)
	location = models.CharField(max_length = 15)
	date = models.CharField(max_length = 20)
	creator = models.CharField(max_length = 15,default='Anonymous')
	updated_at = models.DateTimeField(auto_now = True)
	img = models.CharField(max_length = 200)
	description = models.CharField(max_length = 200)

class Profile(models.Model):
	name = models.CharField(max_length = 15)
	surname = models.CharField(max_length = 15)
	username = models.CharField(max_length = 15)
	location = models.CharField(max_length = 20)
	age = models.CharField(max_length = 2)
	img = models.CharField(max_length = 200)
	hobbies = models.CharField(max_length = 200)
# Create your models here.