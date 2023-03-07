from django.db import models


class Recipe(models.Model):
    """Recipe object"""
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    ingredients = models.CharField(max_length=255)
   # display an instance of the model when necessary


class Book(models.Model):
    titleBook = models.CharField(max_length=255)
    time_minutesBook = models.IntegerField()
    ingredientsBook = models.CharField(max_length=255)
   # display an instance of the model when necessary

    def __str__(self):
        return self.title
