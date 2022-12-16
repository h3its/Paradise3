from django.contrib import admin
from recipes.models import Recipe_Post

# Register your models here.


class Recipe_PostAdmin(admin.ModelAdmin):
    pass



admin.site.register(Recipe_Post, Recipe_PostAdmin)
