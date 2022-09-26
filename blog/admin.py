from django.contrib import admin
from blog.models import Author, Post, Topic

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass
class TopicAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)

