from django.shortcuts import render
from blog.models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')



def all_posts(request):
    #query the db to return all project objects
    posts = Post.objects.all()
    return render(request, 'blog/all_posts.html', {'posts':posts})

def single_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/single_post.html',
                  {'post':post})

def about(request):
    return render(request, 'blog/about.html')
