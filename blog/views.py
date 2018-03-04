from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')	
	return render(request, 'blog/post_list.html', {'posts': posts})






	# posted = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	# context_dict = {}
	# for my_post in posted:
	# 	context_dict[image] = my_post.photo.url
	# return render(request, 'blog/post_list.html', {'posted': posted})		







	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	# for p in Post.objects.all():
	# 	if p.photo:
	# 		photo = p.photo.url
	# 		print(photo)
	# 		p.save()	
	# return render(request, 'blog/post_list.html', {'posts': posts})
