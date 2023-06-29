from django import forms

class FeedbackForm(forms.Form):
    name =  forms.CharField(max_length=100, 
                            min_length=2, 
                            label='Имя', 
                            widget=forms.TextInput(attrs={
                                'placeholder':'Введите Ваше имя',
                                'class':'form-control',
                                }))
    
    phone = forms.CharField(max_length=70, min_length=11,
                        label='Телефон',
                        widget=forms.TextInput(attrs={
                            'placeholder':'Укажите Ваш телефон',
                            'class': 'form-control',
                            }))
    
    email = forms.EmailField(max_length=150, 
                             help_text='Необязательное поле',
                             widget=forms.TextInput(attrs={
                                 'placeholder':'Укажите ваш действущий EMAIL',
                                 'class': 'form-control',
                                 }))
    
