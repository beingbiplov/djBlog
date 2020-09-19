from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from markdown2 import Markdown

class Blog(models.Model):
	title = models.CharField(max_length=150, blank=False, null=False)
	description = models.TextField(blank=False, null=False)
	content = models.TextField(blank=False, null=False)
	content_html = models.TextField()
	thumbnail = models.ImageField(default="placeholder_thumbnail.png", upload_to='thumbnail')
	createdAt = models.DateField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('details', kwargs={'pk': self.pk})

def markdown_to_html(instance, sender, *args, **kwargs):
	markdowner = Markdown()
	html = markdowner.convert(instance.content)

	instance.content_html = html

pre_save.connect(markdown_to_html, sender=Blog)