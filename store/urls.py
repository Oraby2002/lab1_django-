from django.urls import path
from . import views
from .views import * #ProductListView, ProductDeleteView,CategoryListView, CategoryCreateView,CategoryUpdateView, CategoryDeleteView
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [

   # path('', views.product_list, name='product_list'),
   # path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('', ProductListView.as_view(), name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),  
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('products/', views.product_list_create, name='product-list-create'),
    path('products/update/<int:pk>/', views.ProductUpdateAPIView.as_view(), name='product_update'),
    path('products/detail/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail-update-delete'),
  
]

urlpatterns += router.urls
