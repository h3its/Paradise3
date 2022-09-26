from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),
    path('posts', views.all_posts),
    path('single', views.single_post),
    path('about', views.about),
   # path('<int:pk>', views.single_post),
]