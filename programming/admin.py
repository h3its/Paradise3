from django.contrib import admin
from programming.models import Programming_Post

# Register your models here.


class Programming_PostAdmin(admin.ModelAdmin):
    pass



admin.site.register(Programming_Post, Programming_PostAdmin)


