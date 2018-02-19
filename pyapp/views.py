# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

import datetime
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from pyapp.forms import SignUpForm
from pyapp.models import *
from django.shortcuts import render_to_response

# Create your views here.
from pyapp.models import Category, Post


def login_form(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']

        # authenticate first search for the user in database and if found
        # it returns user object
        # and if it didn't find a user it will return None
        user = authenticate(username=name, password=password)

        if user is not None:  # this means we found the user in database
            login(request, user)  # this means we put the user id in the session

            return HttpResponse('logged in succes')

    return render(request, 'login_form.html')


# this is a decorator
# https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-login-required-decorator
@login_required
def logged_in_only(request):
    return HttpResponse('you are authenticated')


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def all_categories(request):
    all_cat = Category.objects.all()
    return JsonResponse(serializers.serialize('json', all_cat), safe=False)


def post_by_category(request, name):
    cat = Category.objects.get(cat_name=name)
    posts = Post.objects.filter(category=cat).order_by('-created_date')
    return JsonResponse(serializers.serialize('json', posts), safe=False)


def show_post(request, post_id):
    post = Post.objects.filter(id=post_id).order_by('-created_date')
    return JsonResponse(serializers.serialize('json', post), safe=False)

def CharStars(text):
    char_no=len(text)
    stars=""
    while char_no!=0 :
        stars+='*'
        char_no-=1
    return stars

def replaceBadWord(comment,bad_words):
    for word in bad_words:
        for ct in comment:
            bad_word=str(word).lower()
            my_comment=ct.text.lower()
            stars=CharStars(bad_word)
            ct.text=my_comment.replace(bad_word,str(stars))
    return comment


def show_comments(request, post_id):
    comment = Comment.objects.filter(post_id=post_id).order_by('-created_date')
    bad_words = BadWords.objects.all()
    comment=replaceBadWord(comment,bad_words)
    return JsonResponse(serializers.serialize('json', comment), safe=False)


def all_posts(request):
    all_post = Post.objects.all()
    return JsonResponse(serializers.serialize('json', all_post), safe=False)


def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    return JsonResponse(serializers.serialize('json', [user]), safe=False)



def sup(request, user_id, cat_id):
    Sup.objects.create(user=User.objects.get(id=user_id), cat=Category.objects.get(id=cat_id))
    return JsonResponse({"state": True}, safe=False)


def un_sup(request, user_id, cat_id):
    ret_sup = Sup.objects.get(user=user_id, cat=cat_id)
    ret_sup.delete()
    return JsonResponse({"state": "unsup"}, safe=False)


def home(request):
   return render_to_response('home.html')

def get_category(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    return JsonResponse(serializers.serialize('json', [cat]), safe=False)


def add_comment(request,text,post):
    date=datetime.datetime.now()
    #u=request.user
    u=User.objects.get(id=1)
    comment = Comment.objects.create(text=text,post=Post.objects.get(id=post),username=User.objects.get(id=1),created_date=date)
    bad_words = BadWords.objects.all()
    comment = replaceBadWord([comment], bad_words)
    return JsonResponse(serializers.serialize('json',comment), safe=False)

def show_reply(request,post_id,comment_id):
    bad_words = BadWords.objects.all()
    reply=Reply.objects.filter(post=Post.objects.get(id=post_id),comment=Comment.objects.get(id=comment_id))
    reply = replaceBadWord(reply, bad_words)
    return JsonResponse(serializers.serialize('json', reply), safe=False)

def add_reply(request,text,post_id,comment_id):
    date=datetime.datetime.now()
    #u=request.user
    u=User.objects.get(id=1)
    bad_words = BadWords.objects.all()
    reply = Reply.objects.create(text=text,comment=Comment.objects.get(id=comment_id),post=Post.objects.get(id=post_id),username=u,created_date=date)
    reply = replaceBadWord([reply], bad_words)
    return JsonResponse(serializers.serialize('json',reply), safe=False)