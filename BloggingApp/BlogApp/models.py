from django.db import models

# Create your models here.
class yesha(models.Model):
	writer = models.CharField(max_length=50)
	blog =  models.CharField(max_length=100)
	price = models.IntegerField()
	noblog = models.IntegerField()

	def __str__(self):
		return self.writer