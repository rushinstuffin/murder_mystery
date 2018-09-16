from django.shortcuts import render

posts = [
	{
		'author': 'KyleB',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'September 11, 2018'

	},
	{
		'author': 'Johnny boy',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'September 12, 2018'}

]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

