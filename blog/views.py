from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    #TODO: Only show the ~5 most recent blogs, create an archive/lookup for dated blogs
    #  once Olive starts producing more content
    #e.g. blogs = Blog.objects.order_by('date')[:5], then use a separate object to pass count
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html/', {'blogs':blogs})

def detail(request, blog_id):
    #Looks up blog by pk (primary key) else delivers a 404 page
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})