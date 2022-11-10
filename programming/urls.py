from django.contrib import admin
from django.urls import path
from programming import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_programming_posts),
    #path('posts', views.all_posts),
    #path('single', views.single_post),
    #path('about', views.about),
    #path('posts/<int:pk>', views.single_post, name="single_post"),
]