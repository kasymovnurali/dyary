from django.db import models
from django.utils import timezone
from django.conf import settings

class Dyary(models.Model):
	time= models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=100)
	exercises = models.BooleanField(default=True)
	SCALE = [(str(i), str(i)) for i in range(1,11)]
	scale = models.CharField(
		max_length=2, 
		default=SCALE[0],
		choices=SCALE)

	def __str__(self):
		return self.status


# Create your models here.
