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
    commentForm = fms.CommentForm()
    posts = mdl.Post.objects.order_by('-updated').all()
    signup_form = ac_fms.SignupForm()
    context = {
        'form':login_form,
        'posts':posts,
        'comment_form':commentForm,
        'signupform':signup_form,
    }
    return render(request, 'posts/index.html', context)

@login_required
def add_blog(request: HttpRequest,*args, **kwargs) -> HttpResponse:
    if request.method == 'POST':
        print("form posted")
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
    signup_form = ac_fms.SignupForm()

    context = {
        'ports':portfolios,
        'form':login_form,
        'signupform':signup_form,
    }
    return render(request, 'posts/about_us.html', context)

def add_comment(request:HttpRequest, post_id:int, *args, **kwargs) -> HttpResponse:
    post = get_object_or_404(mdl.Post, pk=post_id)
    if request.method == 'POST':
        form = fms.CommentForm(data=request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.owner = request.user
            comment.post = post
            comment.save()
            return redirect('posts:home')
        return redirect('accounts:login')
    return redirect('posts:home')

def delete_comment(request:HttpRequest, id:int, *args, **kwargs) -> HttpResponse:
    comment = get_object_or_404(mdl.PostComment, pk=id)
    comment.delete()
    return redirect('posts:home')

def send_complain(request:HttpRequest, *args, **kwargs) -> HttpResponse:
    complains = mdl.Complain.objects.all()
    if request.method == 'POST':
        form = fms.ComplainForm(data=request.POST)
        if form.is_valid():
            new_complain = form.save(commit=False)
            new_complain.user = request.user
            new_complain.save()
            return redirect('posts:user-complains')
    else:
        complain_form = fms.ComplainForm()

    context = {
        'complain_form':complain_form,
        'complains':complains
    }
    return render(request, 'posts/user_complains.html',context)

def complain_details(request:HttpRequest, id:int, *args, **kwargs) -> HttpResponse:
    complain = get_object_or_404(mdl.Complain, pk=id)
    if request.method == 'POST':
        form = fms.FeedBackForm(data=request.POST)
        if form.is_valid():
            new_feedback = form.save(commit=False)
            new_feedback.user = request.user
            new_feedback.complain = complain
            new_feedback.save()
            return redirect('posts:complain_details', id)
    else:
        form = fms.FeedBackForm()
    context =  {
        'form':form,
        'complain':complain
    }
    return render(request, 'posts/complain_details.html', context)

def feedback_list(request:HttpRequest, *args, **kwargs) -> HttpResponse:
    feedbacks = mdl.FeedBack.objects.all()
    context =  {
        'feedbacks':feedbacks
    }
    return render(request, 'posts/feedbacks.html',context)

def complain_list(request:HttpRequest, *args, **kwargs) -> HttpResponse:
    complains = mdl.Complain.objects.all()
    context =  {
        'complains':complains
    }
    return render(request, 'posts/complains.html',context)