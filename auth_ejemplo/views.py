from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.


def home(request):
    return render(request, 'auth/home.html')


@login_required
def dashboard(request):
    return render(request, 'auth/dashboard.html')


def custom_logout(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('home')