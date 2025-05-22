from django import forms
from .models import Product , Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class meta:
        model = Category
        fields = {'name','slug','description'}


