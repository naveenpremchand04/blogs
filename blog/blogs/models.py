from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=64)
	post = models.CharField(max_length=140)
	created = models.DateTimeField(auto_now = True)

# Create your models here.
