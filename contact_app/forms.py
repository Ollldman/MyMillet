# contact/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя',
                'required': True  # Явно указываем, что поле обязательно
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш email',
                'required': True
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема сообщения',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control-area',
                'placeholder': 'Ваше сообщение',
                'rows': 5,
                'required': True
            }),
        }
        labels = {
            'name': 'Имя',
            'email': 'Электронная почта',
            'subject': 'Тема',
            'message': 'Сообщение',
        }