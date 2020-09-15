from django.shortcuts import render
from datetime import datetime

def index(request):

	# Dummy data for front-end
	posts = [
		{
			'title' : 'Blog post title.',
			'description' : 'This is a short description of the blog post consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.',
			'content' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.',
			'createdAt' : datetime.now().strftime('%D %H:%M'),
		},
		{
			'title' : 'New post title.',
			'description' : 'This is a short description of the blog post',
			'content' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.',
			'createdAt' : datetime.now().strftime('%D %H:%M'),
		}
	]

	context = {
		'posts' : posts
	}

	return render(request, 'core/index.html', context)