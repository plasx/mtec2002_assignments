from django.db import models

# Create your models here.

class Todo(models.Model):
		name = models.CharField(max_length=200)
		finished = models.BooleanField()
		
