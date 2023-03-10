from django.db import models
# from django.utils.crypto import get_random_string


def random_id():
    random_str = get_random_string(3, allowed_chars='0123456789')
    return int(random_str)


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
    # id = models.CharField(primary_key=True, max_length=2,
    #                       default=get_random_string,)
    doctor_id = models.IntegerField(
        primary_key=True, default=random_id, editable=False)
    reviseNo = models.IntegerField()
    code = models.CharField(max_length=3, null=True)
    firstNameTH = models.CharField(max_length=50)
    lastNameTH = models.CharField(max_length=50)
    firstNameEN = models.CharField(max_length=50)
    lastNameEN = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True)
    remark = models.CharField(max_length=250, null=True)
    isActive = models.BooleanField()
    reviseBy = models.IntegerField()
    reviseDate = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.Recipe


def __str__(self):
    return self.Book
