from django.urls import path
from core import views
urlpatterns = [
    path('form_ok/', views.lid_tel_form, name='callback'),
    path('form_modal_ok/', views.modal_form, name='modal_form'),
    path('form_contact_ok/', views.form_contact, name='form_contact'),
    path('form_error/', views.form_error),
    path('search/', views.search, name='search'),
]