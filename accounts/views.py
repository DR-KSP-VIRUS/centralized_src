from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate

from . import models as mdl
from . import forms as fms

# Create your views here.

def user_login_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = fms.LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user=user)
                return redirect('accounts:dashboard')
            return redirect('posts:home')
        return redirect('posts:home')
    return redirect('posts:home')
            
def user_dashboard(request:HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'accounts/dashboard.html',context)

def user_logout(request:HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('posts:home')