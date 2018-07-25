from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from mysite.Blog.models import BlogPost

def home(request):
	posts = BlogPost.objects.all()
	t = loader.get_template("home.html")
	c = {'posts':posts}
	return HttpResponse(t.render(c))

# Create your views here.
