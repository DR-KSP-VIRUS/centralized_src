from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpRequest, HttpResponse


from . import forms as fms 
from accounts import forms as ac_fms
from . import models as mdl

# Create your views here.


def index(request):
    login_form = ac_fms.LoginForm()
    context = {
        'form':login_form
    }
    return render(request, 'posts/index.html', context)

def add_blog(request: HttpRequest) -> HttpResponse:
    context = {}
    return redirect('posts:new-blogs')

def new_blogs(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'posts/new_blogs.html', context)

def blogs(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'posts/blogs.html', context)