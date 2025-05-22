from django.urls import path
from . import views
from .views import * #ProductListView, ProductDeleteView,CategoryListView, CategoryCreateView,CategoryUpdateView, CategoryDeleteView

urlpatterns = [

   # path('', views.product_list, name='product_list'),
   # path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('', ProductListView.as_view(), name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),  
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/add/', CategoryCreatView.as_view(), name='category_add'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('products/', views.product_list_create, name='product-list-create'),

]
