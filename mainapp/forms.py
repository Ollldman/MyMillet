
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Имя пользователя'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Почта'
                }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Пароль'
                }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Повторите пароль'
            })
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user