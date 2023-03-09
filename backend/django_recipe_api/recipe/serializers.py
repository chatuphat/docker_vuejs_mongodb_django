from dataclasses import fields
from rest_framework import serializers
from .models import Recipe, Book, Doctors

# create a serializer


class RecipeSerializer(serializers.ModelSerializer):
    # initialize model and fields you want to serialize
    class Meta:
        model = Recipe
        fields = ['title',
                  'time_minutes',
                  'ingredients']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['titleBook',
                  'time_minutesBook',
                  'ingredientsBook']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['reviseNo',
                  'code',
                  'reviseDate'
                  ]
