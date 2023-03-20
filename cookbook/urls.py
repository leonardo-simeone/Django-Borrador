from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('recipe/<str:pk>/', views.recipeUnits, name='recipeunit'),
    path('add-recipe/', views.createRecipe, name='add-recipe'),
    path('update-recipe/<str:pk>/', views.updateRecipe, name='update-recipe'),
    path('delete/<str:pk>/', views.deleteRecipe, name='delete'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
    path('gallery/', views.gallery, name='gallery'),
]