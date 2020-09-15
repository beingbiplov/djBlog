from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView

class indexListView(ListView):
	model = Blog
	template_name = 'core/index.html'
	context_object_name= 'posts'
	ordering = ['-createdAt']