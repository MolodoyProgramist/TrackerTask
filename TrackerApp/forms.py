from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import DateInput
from .models import  Task, Comment


class TaskForm(forms.ModelForm):
     class Meta:
         model = Task
         fields = ['title', 'description', 'author', 'status', 'priority', 'deadline']

         widgets = {
             'deadline': forms.DateTimeInput(attrs={
                 'type': 'datetime-local',
                 'class': 'form-control',
             }),
         }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text','author','task', 'media', 'comment']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    birth_date = forms.DateField(label='Дата народження', widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError('Паролі не співпадають')
        return cd.get('password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Ім’я користувача')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)