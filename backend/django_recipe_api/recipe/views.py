from django.shortcuts import render


from rest_framework import viewsets

from .serializers import RecipeSerializer, BookSerializer, DoctorSerializer
from .models import Recipe, Book, Doctors


class recipe_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class book_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class doctor_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
