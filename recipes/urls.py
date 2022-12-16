from django.contrib import admin
from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.all_recipe_posts),
    #path('posts', views.all__recipe_posts),
    #path('single', views.single_post),
    #path('about', views.about),
    path('posts/<int:pk>', views.single_recipe_post, name="single_recipe_post"),
]