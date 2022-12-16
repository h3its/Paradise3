from django.shortcuts import render
from recipes.models import  Recipe_Post

# Create your views here.
def all_recipe_posts(request):
    #query the db to return all project objects
    recipe_posts = Recipe_Post.objects.all()
    return render(request, 'recipes/all_recipe_posts.html', {'programming_posts':recipe_posts})


def single_recipe_post(request, pk):
    recipe_post = Recipe_Post.objects.get(pk=pk)
    return render(request, 'recipes/single_recipe_post.html', {'programming_post':recipe_post})
