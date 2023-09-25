from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class PostListView(ListView):
    model = Post
    template_name = "trees/home.html"
    context_object_name = 'post'
    ordering = ["-date_posted"]
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def home(request):
    context =  {
        "posts": Post.objects.all()
    }
    return render(request, "trees/home.html", context)

def about(request):
    return render(request, "trees/about.html", {"title":"about"})
