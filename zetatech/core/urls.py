from django.urls import path
from core import views

urlpatterns = [
    path('feedback/', views.send_email, name='feedback'),
]