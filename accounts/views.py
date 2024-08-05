from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from . import models as mdl
from . import forms as fms
from posts import models as pmdl

# Create your views here.

def user_login_form(request: HttpRequest,*args, **kwargs) -> HttpResponse:
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

@login_required
def user_dashboard(request:HttpRequest,*args, **kwargs) -> HttpResponse:
    posts = pmdl.Post.objects.order_by('-updated').all()

    context = {
        'posts':posts
    }
    return render(request, 'accounts/dashboard.html',context)

@login_required
def user_logout(request:HttpRequest, *args, **kwargs) -> HttpResponse:
    logout(request)
    return redirect('posts:home')

@login_required
def add_portfolio(request:HttpRequest,*args, **kwargs) -> HttpResponse:
    form = fms.PortfolioForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        portfolio = form.save(commit=False)
        portfolio.user = request.user
        portfolio.save()
        return redirect('accounts:portfolios')
    return redirect('accounts:portfolios')

@login_required
def portfolios(request:HttpRequest,*args, **kwargs) -> HttpResponse:
    form = fms.PortfolioForm()
    ports = mdl.Portfolio.objects.all()
    context={
        "form":form,
        'ports':ports
    }
    return render(request, 'accounts/portfolio.html', context)

@login_required
def remove_portfoloio(request:HttpRequest, id:int, *args, **kwargs) -> HttpResponse:
    portfolio = get_object_or_404(mdl.Portfolio, pk=id)
    portfolio.delete()
    return redirect('accounts:portfolios')

@login_required
def edit_portfolio(request:HttpRequest, id:int, *args, **kwargs)->HttpResponse:
    portfolio = get_object_or_404(mdl.Portfolio, pk=id)
    if request.method == "POST":
        form = fms.PortfolioForm(instance=portfolio, data=request.POST, files=request.FILES)
        if form.is_valid():
            port = form.save(commit=False)
            port.user = request.user
            port.save()
            return redirect('accounts:edit-portfolio',id=portfolio.id)
    else:
        form = fms.PortfolioForm(instance=portfolio)
    context = {
        'form':form,
        'portfolio':portfolio
    }

    return render(request, 'accounts/edit_portfolio.html', context)