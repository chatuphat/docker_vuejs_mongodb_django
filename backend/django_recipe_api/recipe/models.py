from django.db import models
from django.utils.crypto import get_random_string


class Recipe(models.Model):
    """Recipe object"""
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    ingredients = models.CharField(max_length=255)


class Book(models.Model):
    titleBook = models.CharField(max_length=255)
    time_minutesBook = models.IntegerField()
    ingredientsBook = models.CharField(max_length=255)


class Doctors(models.Model):
    id = models.CharField(primary_key=True, max_length=12,
                          default=get_random_string,)
    reviseNo = models.IntegerField()
    code = models.CharField(max_length=3)
    reviseDate = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.Recipe


def __str__(self):
    return self.Book
