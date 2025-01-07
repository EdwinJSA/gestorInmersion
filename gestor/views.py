from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *

# Vista de inicio
def inicio(request):
    return render(request, 'index.html')

# Vista de login
def login_view(request):  # Evita el conflicto con `django.contrib.auth.login`
    if request.user.is_authenticated:
        return redirect('home')  # Evita que usuarios autenticados vean el login

    form = loginForm()
    return render(request, 'login.html', {'form': form})

# Vista de validación de usuario
def validarUsuario(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if not form.is_valid():
            return render(request, 'login.html', {'form': form})

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        usuario = authenticate(request, username=username, password=password)
        
        if usuario:
            auth_login(request, usuario)  # Inicia sesión correctamente
            return redirect('home')
        else:
            form.add_error(None, 'Usuario o contraseña incorrectos')

    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')