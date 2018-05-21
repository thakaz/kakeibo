from django.db import models

# Create your models here.

class Payment(models.Model):
    this_date = models.DateTimeField()
    category1 = models.IntegerField()
    category2 = models.IntegerField()
    place     = models.CharField(max_length=100)
    payment   = models.IntegerField()
    summary   = models.CharField(max_length=100)

class Category1(models.Model):
    number1        = models.IntegerField()
    category_name = models.CharField(max_length=100)

class Category2(models.Model):
    number1       = models.IntegerField()
    number2       = models.IntegerField()
    category_name = models.CharField(max_length=100)


