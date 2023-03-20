from django.shortcuts import render, redirect
from .models import NewRecipe, Comment
from .forms import NewRecipeForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def registerView(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('recipes')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('login')


def recipes(request):
    recipes_list = NewRecipe.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(recipes_list, 3)

    try:
        recipes_list = paginator.page(page)
    except PageNotAnInteger:
        recipes_list = paginator.page(1)
    except EmptyPage:
        recipes_list = paginator.page(paginator.num_pages)

    context = {'recipes_list': recipes_list}
    return render(request, 'recipes.html', context)


def recipeUnits(request, pk):
    recipe_object = NewRecipe.objects.get(id=pk)
    tags = recipe_object.tags.all()
    # comments = recipe_object.comment_set.all()
    # --->  this one is saying: from recipe_object give me all the comment children
    # (it won't work if we have a related name in the models only the second call will work)
    # but if we add a related name 'comments' then we can access it by:
    comments = recipe_object.comments.all()
    context = {'recipe_object': recipe_object, 'tags': tags, 'comments': comments}
    return render(request, 'recipe.html', context)


def createRecipe(request):
    form = NewRecipeForm()

    if request.method == 'POST':
        form = NewRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes')

    context = {'form': form}
    return render(request, 'recipe-form.html', context)


def updateRecipe(request, pk):
    recipe = NewRecipe.objects.get(id=pk)
    form = NewRecipeForm(instance=recipe)

    if request.method == 'POST':
        form = NewRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes')

    context = {'form': form}
    return render(request, 'recipe-form.html', context)


def deleteRecipe(request, pk):
    recipe = NewRecipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')

    return render(request, 'delete.html', {'object': recipe})


def gallery(request):
    return render(request, 'gallery.html', {})
