from django.urls import path
from . import views
urlpatterns = [
    path('catalog/', views.product ),
    path('catalog/<slug>/', views.product_detail ),
]
