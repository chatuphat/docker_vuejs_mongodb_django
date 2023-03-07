from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
# impor the serializer we just created
from .serializers import RecipeSerializer
from .serializers import BookSerializer
from .models import Recipe
from .models import Book


class recipe_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class book_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Book.objects.all()
    serializer_class = BookSerializer
