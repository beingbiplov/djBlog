from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

class indexListView(ListView):
	model = Blog
	template_name = 'core/index.html'
	context_object_name= 'posts'
	ordering = ['-createdAt']
	paginate_by = 5

class blogDetailView(DetailView):
	model = Blog
	template_name = 'core/blog_details.html'
	context_object_name= 'post'

class blogDeleteView(DeleteView):
	model = Blog
	template_name = 'core/delete.html'
	context_object_name= 'post'
	success_url = '/'

class blogCreateView(CreateView):
	model = Blog
	fields = ['title', 'description', 'content', 'thumbnail']
	template_name = 'core/blog_create.html'

class blogUpdateView(UpdateView):
	model = Blog
	template_name = 'core/blog_edit.html'
	fields = ['title', 'description', 'content', 'thumbnail']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		blog_pk = self.kwargs['pk']
		context['blog_pk'] = blog_pk

		return context