from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from core.form import FeedbackForm
# Create your views here.

def send_email(request):
    if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                # Обработка данных формы
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                consent = form.cleaned_data['consent']
                # Дополнительная логика
                # ...
                return   # Замените 'success.html' на ваш шаблон успеха
    else:
        form = FeedbackForm()
    return  {'form': form}