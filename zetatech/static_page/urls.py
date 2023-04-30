from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('faq/', views.faq, name="faq"),
    path('contact/', views.contact, name="contact"),
    path('offer/', views.offer, name="offer"),
]