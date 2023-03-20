from django.contrib import admin
from .models import NewRecipe, Comment, Tag

# Register your models here.

admin.site.register(NewRecipe)
admin.site.register(Comment)
admin.site.register(Tag)
