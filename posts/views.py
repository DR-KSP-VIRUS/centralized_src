from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

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

@login_required
def add_blog(request: HttpRequest,*args, **kwargs) -> HttpResponse:
    if request.method == 'POST':
        form = fms.BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            return redirect('posts:blogs')
    return redirect('posts:blogs')

@login_required
def blogs(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    form = fms.BlogForm()
    posts = mdl.Post.objects.order_by('-updated').all()
    context = {
        'form':form,
        'posts':posts
    }
    return render(request, 'posts/blogs.html', context)

@login_required
def blog_details(request:HttpRequest, id:int, *args, **kwargs) -> HttpResponse:
    post = get_object_or_404(mdl.Post,pk=id)
    context = {
        'post':post
    }
    return render(request, 'posts/blog_details.html', context)

@login_required
def edit_blog(request:HttpRequest, id:int, *args, **kwargs)->HttpResponse:
    post = get_object_or_404(mdl.Post, pk=id)
    if request.method == 'POST':
        form = fms.BlogForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.owner = request.user
            update.save()
            return redirect('posts:blog_details',id=post.id)
    else:
        form = fms.BlogForm(instance=post)
    context = {
        'post':post,
        'form':form
    }

    return render(request, 'posts/edit_blog.html', context)

@login_required
def remove_blog(request:HttpRequest, id:int, *args, **kwargs) -> HttpResponse:
    post = get_object_or_404(mdl.Post, pk=id)
    post.delete()
    return redirect('posts:blogs')

def about_us(request:HttpRequest, *args, **kwargs):
    portfolios = ac_mdl.Portfolio.objects.all()
    login_form = ac_fms.LoginForm()
    context = {
        'ports':portfolios,
        'form':login_form
    }
    return render(request, 'posts/about_us.html', context)