from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from core.form import Lid_Tel_Form
# Create your views here.

def lid_tel_form(request):
    if request.method == 'POST':
            form = Lid_Tel_Form(request.POST)
            if form.is_valid():
                # Обработка данных формы
                phone = form.cleaned_data['phone']
                # Дополнительная логика
                # ...
                return   # Замените 'success.html' на ваш шаблон успеха
    else:
        form = Lid_Tel_Form()
    return  {'lid_tel_form': form}