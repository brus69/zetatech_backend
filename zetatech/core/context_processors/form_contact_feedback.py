from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from core.form import Form_Contact_Feedback
# Create your views here.

def form_contact_feedback(request):
    if request.method == 'POST':
            form = Form_Contact_Feedback(request.POST)
            if form.is_valid():
                # Обработка данных формы
                name = form.changed_data['name']
                phone = form.cleaned_data['phone']
                email = form.changed_data['email']
                text = form.changed_data['text']
                # Дополнительная логика
                # ...
                return   # Замените 'success.html' на ваш шаблон успеха
    else:
        form = Form_Contact_Feedback()
    return  {'form_contact_feedback': form}