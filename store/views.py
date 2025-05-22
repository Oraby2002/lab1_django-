from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import Product, Category
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = SignUpForm()
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/update_product.html', {'form': form})




class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

class ProductDeleteView(DeleteView):  
    model = Product
    template_name = 'store/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

class CategoryListView(ListView):
    model= Category
    template_name = 'store/category_list.html'
    context_object_name= 'categories'

class CategoryCreatView(CreateView):
    model= Category
    fields = ['name', 'slug', 'description']
    template_name= 'store/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model= Category
    fields = ['name', 'slug', 'description']
    fields = ['name', 'slug', 'description']
    template_name= 'store/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name ='store/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
