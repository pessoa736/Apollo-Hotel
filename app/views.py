from django.shortcuts import render
from .models import Post

# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'index.html')

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')
