from distutils.command.upload import upload
from re import T
from statistics import mode
from tkinter import CASCADE
from tokenize import blank_re
from turtle import title
from unicodedata import category, name
from django.db import models

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    s =[
        ('available','available'),
        ('rented','rented'),
        ('sold','sold'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True)
    book_img = models.ImageField(upload_to='photo', null=True, blank=True)
    auth_img = models.ImageField(upload_to='photo', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    sell_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rent_price_per_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rent_days = models.IntegerField(null=True, blank=True)
    rent_profit = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=s, null=True, blank=True)
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title