from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog


def index(request):

  blog = Blog.objects.all()[:10]
  
  context = {
    'title': 'Latest posts',
    'blog':blog
  }

  return render(request, 'blog/index.html', context)

# def details(request, id):
#   blogs=Blog.objects.get(id=id)
#   context = {
#     'blogs': blogs
    
#   }

#   return render(request, 'blog/details.html', context)