from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class NewRecipe(models.Model):
    # creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_creator', null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    number_of_ingredients = models.IntegerField(default=0)
    instructions = models.TextField(null=True, blank=True)
    short_description = models.CharField(max_length=200, null=True, blank=True)
    dish_image = CloudinaryField('image', default="default-image")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title



class Comment(models.Model):
    # creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_creator', null=True, blank=True)
    new_recipe = models.ForeignKey(NewRecipe, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.new_recipe} {self.body}"



