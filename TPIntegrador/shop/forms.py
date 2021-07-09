from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Products

class CustomUserCreationForm(UserCreationForm):
    pass

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'