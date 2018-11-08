from django.contrib.gis.db import models

class User(models.Model):
	name = models.TextField()
	location = models.PointField(geography=True, null=True, blank=False)
	
	def __str__(self):
		return self.name
	
