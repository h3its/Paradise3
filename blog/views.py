from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def all_posts(request):
    return render(request, 'blog/all_posts.html')

def single_post(request):
    return render(request, 'blog/single_post.html')

def about(request):
    return render(request, 'blog/about.html')
