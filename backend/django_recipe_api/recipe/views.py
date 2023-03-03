from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
# impor the serializer we just created
from .serializers import RecipeSerializer
from .models import Recipe


class recipe_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
