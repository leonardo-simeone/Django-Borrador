from django.forms import ModelForm
from .models import NewRecipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewRecipeForm(ModelForm):
    class Meta:
        model = NewRecipe
        fields = ['title', 'number_of_ingredients', 'instructions', 'short_description', 'dish_image', 'tags']
        # We can output all the fields in the form by saying:
        # fields = '__all__'  --> is we do this then we have to reference each filed we want on the form
        # individually in html like so: {{form.title}}  {{form.name}} {{form.ingredients}} and so on
        # exclude = ['created', 'updated', 'id'] --> if we do this, these fields will be excluded from the form
        # they will be excluded from '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
