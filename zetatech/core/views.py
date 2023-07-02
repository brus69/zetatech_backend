from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from .form import FeedbackForm, Lid_Tel_Form, Form_Contact_Feedback
from zetatech.settings import *

# Create your views here.

def lid_tel_form(request):
    if request.method == 'POST':
            form = Lid_Tel_Form(request.POST)
            if form.is_valid():
                # Обработка данных формы
                phone = form.cleaned_data['phone']
                # Дополнительная логика
                subject = 'Заявка на обратный звонок лид форма'
                message = f'Телефон: {phone}'
                from_email = DEFAULT_FROM_EMAIL
                recipient_list = [NOTIFY_EMAIL]
                send_mail(subject, message, from_email, recipient_list)
                return  render(request, "static_page/form_ok.html")
    else: 
        return  redirect("form_error/")
   
def modal_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            from_email = form.cleaned_data['email']
            subject = 'Заявка модальное окно'
            message = f'Имя: {name}, Телефон: {phone}'
            recipient_list = [NOTIFY_EMAIL]
            send_mail(subject, message, from_email, recipient_list)
            return render(request, 'static_page/form_ok.html')
    else:
         return redirect('form_error/')

def form_contact(request):
    if request.method == 'POST':
        form = Form_Contact_Feedback(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            from_email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            check_box_form = form.cleaned_data['check_box_form']
            subject = 'Заявка с контактной формы'
            message = f'Имя: {name}, Телефон: {phone}, Текст: {text}, Обработка персональных данных: {check_box_form}'
            recipient_list = [NOTIFY_EMAIL]
            send_mail(subject, message, from_email, recipient_list)
            return render(request, 'static_page/form_ok.html')
        else:
             return redirect('form_error/')

def form_error(request):
     return render(request, "static_page/form_error.html")