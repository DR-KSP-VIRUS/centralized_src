from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpRequest, HttpResponse


from . import forms as fms 
from accounts import forms as ac_fms
from . import models as mdl
from accounts import models as ac_mdl

# Create your views here.


def index(request,*args, **kwargs):
    login_form = ac_fms.LoginForm()
    context = {
        'form':login_form
    }
    return render(request, 'posts/index.html', context)

def add_blog(request: HttpRequest,*args, **kwargs) -> HttpResponse:
    context = {}
    return redirect('posts:new-blogs')

def new_blogs(request: HttpRequest,*args, **kwargs) -> HttpResponse:
    context = {}
    return render(request, 'posts/new_blogs.html', context)

def blogs(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    context = {}
    return render(request, 'posts/blogs.html', context)

def about_us(request:HttpRequest, *args, **kwargs):
    portfolios = ac_mdl.Portfolio.objects.all()
    login_form = ac_fms.LoginForm()
    context = {
        'ports':portfolios,
        'form':login_form
    }
    return render(request, 'posts/about_us.html', context)