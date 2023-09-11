from http.client import HTTPResponse
from django.shortcuts import render
from .models import Post
# Create your views here.

posts = [
    {
        "author": "JacksonM",
        "title": "Trees Request 1",
        "content": "First request",
        "date_posted": "September 10th, 2023"
    },
    {
        "author": "John Doe",
        "title": "Trees Request 2",
        "content": "Second request",
        "date_posted": "September 11th, 2023"
    }

]

def home(request):
    context =  {
        "posts": Post.objects.all()
    }
    return render(request, "trees/home.html", context)

def about(request):
    return render(request, "trees/about.html", {"title":"about"})
