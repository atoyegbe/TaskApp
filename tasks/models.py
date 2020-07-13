from django.db import models

# Create your models here.
class TaskApp(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	is_complete = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title





	
