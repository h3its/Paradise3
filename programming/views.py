from django.shortcuts import render
from programming.models import  Programming_Post

# Create your views here.
def all_programming_posts(request):
    #query the db to return all project objects
    programming_posts = Programming_Post.objects.all()
    return render(request, 'programming/all_programming_posts.html', {'programming_posts':programming_posts})


def single_programming_post(request, pk):
    programming_post = Programming_Post.objects.get(pk=pk)
    return render(request, 'programming/single_programming_post.html', {'programming_post':programming_post})
