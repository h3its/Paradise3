from django.shortcuts import render

# Create your views here.
def all_programming_posts(request):
    #query the db to return all project objects
    #posts = Post.objects.all()
    return render(request, 'programming/all_programming_posts.html')
    #{'posts': posts}