from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Book, Catagory
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'book_img',
            'auth_img',
            'sell_price',
            'pages',
            'rent_price_per_day',
            'rent_days',
            'rent_profit',
            'status',
            'category',
        ]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control'}),
            'book_img' : forms.FileInput(attrs={'class' : 'form-control'}),
            'auth_img' : forms.FileInput(attrs={'class' : 'form-control'}),
            'sell_price' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'pages' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'rent_price_per_day' : forms.NumberInput(attrs={'class' : 'form-control', 'id' : 'rent_price_per_day'}),
            'rent_days' : forms.NumberInput(attrs={'class' : 'form-control', 'id' : 'rent_days'}),
            'rent_profit' : forms.NumberInput(attrs={'class' : 'form-control', 'id' : 'rent_profit'}),
            'status' : forms.Select(attrs={'class' : 'form-control'}),
            'category' : forms.Select(attrs={'class' : 'form-control'}),
        }