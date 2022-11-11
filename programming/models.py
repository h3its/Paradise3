from django.db import models

# Create your models here.
class Programming_Post(models.Model):
    Post_Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Body = models.TextField()
    Date = models.DateField(auto_now_add=True)
    Author = models.ForeignKey('blog.Author', on_delete=models.CASCADE)
    def __str__(self):
        return self.Title