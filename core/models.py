from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=150, blank=False, null=False)
	description = models.TextField(blank=False, null=False)
	content = models.TextField(blank=False, null=False)
	createdAt = models.DateField(auto_now=True)
	thumbnail = models.ImageField(default="placeholder_thumbnail.png", upload_to='thumbnail')


	def __str__(self):
		return self.title