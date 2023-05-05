from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.product, name='catalog'),
    path('catalog/<slug>/', views.product, name='catalog_category'),
    path('<slug:product_slug>/', views.product_detail, name='product_detail'),
]