from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView

class indexListView(ListView):
	model = Blog
	template_name = 'core/index.html'
	context_object_name= 'posts'
	ordering = ['-createdAt']

class blogDetailView(DetailView):
	model = Blog
	template_name = 'core/blog_details.html'
	context_object_name= 'post'
