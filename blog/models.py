from django.db import models

# Create your models here.
class Author(models.Model):
    Author_Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Bio = models.TextField(max_length=120)

    def __str__(self):
        return self.Name

class Topic(models.Model):
    Topic_Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Post(models.Model):
    Post_Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Body = models.TextField()
    Date = models.DateField(auto_now_add=True)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    Image = models.CharField(max_length=100)
    def __str__(self):
        return self.Title
