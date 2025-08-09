from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import authenticate, logger
from django.template.context_processors import request
from django.contrib import messages

from TrackerApp.forms import UserRegistrationForm, UserLoginForm
from TrackerApp.models import Task

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # создаём профиль с датой рождения
            #Task.objects.create(user=new_user, birth_date=form.cleaned_data['birth_date'])
            return redirect('task-list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task-list')  # главная страница после входа
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('home')  # или куда хочеш перенаправити
# Create your views here.
