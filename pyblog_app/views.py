from django.shortcuts import render
from  django.http import HttpResponse
from pyapp.models import Category,Post,Comment,Reply,BadWords
from django.contrib.auth.models import User
from .forms import PostForm
from django.http import HttpResponseRedirect
import datetime
# Create your views here.
def admin(request):
    return render(request, 'Admin/index.html')

def nav(request):
    return render(request, 'Admin/navbar.html')
def table(request):
    return render(request, 'Admin/tables.html')

def allPosts(request):
    all_posts=Post.objects.all()
    context={'all_posts': all_posts}
    return render(request, 'Admin/posts_tables.html', context)

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/allposts')
    context={'form':form}
    return render(request, 'Admin/post.html',context)