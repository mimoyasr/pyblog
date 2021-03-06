# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from pyapp.forms import SignUpForm
from pyapp.models import *
from django.shortcuts import render_to_response
from pyblog.settings import BASE_DIR
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
from pyapp.models import Category, Post


def login_form(request):
    msg = None;
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user:
            global msg
            if user.is_active == 1:  # this means we found the user in database
                login(request, user)  # this means we put the user id in the session
                var = request.user.is_authenticated()
                admin = request.user.is_superuser
                #return render(request, "home.html", {'user': var, 'admin': admin})
                return HttpResponseRedirect('/home')
            if user.is_active == 0:
                return render(request, 'login_form.html', {"msg": "You're account is disabled"})
        else:
            return render(request, 'login_form.html', {"msg": "wrong username or password"})
    else:
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
            var = request.user
            admin = request.user.is_superuser
            # return HttpResponse(var.id)
            # return HttpResponseRedirect('/home')
            return render(request, "home.html", {'user': var, 'admin': admin})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def all_categories(request):
    all_cat = Category.objects.all()
    cats = []
    for cat in all_cat:
        cats.append({"state": is_supped(request, cat), "cat": serializers.serialize('json', [cat])})
    return JsonResponse(json.dumps(cats), safe=False)


def is_supped(request, cat):
    #JsonResponse(request.user, safe=False)
    # Sup.objects.get(sub_user=request.user, sub_cat=cat)
    try:
        Sup.objects.get(sub_user=request.user, sub_cat=cat)
        return True
    except:
        return False


def post_by_category(request, name):
    cat = Category.objects.get(cat_name=name)
    posts = Post.objects.filter(category=cat).order_by('-created_date')
    return JsonResponse(serializers.serialize('json', posts), safe=False)


def show_post(request, post_id):
    post = Post.objects.filter(id=post_id).order_by('-created_date')
    return JsonResponse(serializers.serialize('json', post), safe=False)


def CharStars(text):
    char_no = len(text)
    stars = ""
    while char_no != 0:
        stars += '*'
        char_no -= 1
    return stars


def replaceBadWord(comment, bad_words):
    for word in bad_words:
        for ct in comment:
            bad_word = str(word).lower()
            my_comment = ct.text.lower()
            stars = CharStars(bad_word)
            ct.text = my_comment.replace(bad_word, str(stars))
    return comment


def show_comments(request, post_id):
    comment = Comment.objects.filter(post_id=post_id).order_by('-created_date')
    bad_words = BadWords.objects.all()
    comment = replaceBadWord(comment, bad_words)
    return JsonResponse(serializers.serialize('json', comment), safe=False)


def all_posts(request):
    all_post = Post.objects.all()
    for post in all_post:
        post.dir = BASE_DIR
    return JsonResponse(serializers.serialize('json', all_post), safe=False)


def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    return JsonResponse(serializers.serialize('json', [user]), safe=False)


def sup(request, cat_id):
    Sup.objects.create(sub_user=request.user, sub_cat=Category.objects.get(id=cat_id))
    return JsonResponse({"state": True}, safe=False)


def un_sup(request, cat_id):
    ret_sup = Sup.objects.get(sub_user=request.user, sub_cat=cat_id)
    ret_sup.delete()
    return JsonResponse({"state": "unsup"}, safe=False)


def home(request):
    if request.user:
        admin = request.user.is_superuser
        return render(request, "home.html", {'user': request.user.is_authenticated(), 'admin': admin})
    else:
        return render_to_response('home.html')


def base_dir(request):
    return JsonResponse({"base_dir": BASE_DIR + "/admin/static/"}, safe=False)


def logout(request):
    logout(request)
    return HttpResponse('Done')


def get_category(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    return JsonResponse(serializers.serialize('json', [cat]), safe=False)


def add_comment(request, text, post):
    date = datetime.datetime.now()
    u = request.user
    comment = Comment.objects.create(text=text, post=Post.objects.get(id=post), username=u,
                                     created_date=date)
    bad_words = BadWords.objects.all()
    comment = replaceBadWord([comment], bad_words)
    return JsonResponse(serializers.serialize('json', comment), safe=False)


def show_reply(request, post_id, comment_id):
    bad_words = BadWords.objects.all()
    reply = Reply.objects.filter(post=Post.objects.get(id=post_id), comment=Comment.objects.get(id=comment_id))
    reply = replaceBadWord(reply, bad_words)
    return JsonResponse(serializers.serialize('json', reply), safe=False)


def add_reply(request, text, post_id, comment_id):
    date = datetime.datetime.now()
    u = request.user
    bad_words = BadWords.objects.all()
    reply = Reply.objects.create(text=text, comment=Comment.objects.get(id=comment_id),
                                 post=Post.objects.get(id=post_id), username=u, created_date=date)
    reply = replaceBadWord([reply], bad_words)
    return JsonResponse(serializers.serialize('json', reply), safe=False)


def search(request, term):
    cat = Post.objects.filter(Q(title__icontains=term) | Q(tags=Tag.objects.filter(name__icontains=term)))
    return JsonResponse(serializers.serialize('json', cat), safe=False)


def show_likes(request, post_id):
    like = Likes.objects.filter(post_id=post_id).count()
    return JsonResponse(like, safe=False)


def show_dislikes(request, post_id):
    dislike = Dislikes.objects.filter(post_id=post_id).count()
    return JsonResponse(dislike, safe=False)


def add_like(request, post_id):
    u = request.user.id
    like = Likes.objects.filter(post_id=post_id, user_id=u)
    if (like.exists()):
        like.delete()
        result = 'unlike'
    else:
        like = Likes.objects.create(post_id=post_id, user_id=u)
        result = 'like'
    return JsonResponse(result, safe=False)


def add_dislike(request, post_id):
    u = request.user.id
    dislike = None
    try:
        dislike = Dislikes.objects.get(post_id=post_id, user_id=u)
    except:
        pass
    if (dislike):
        dislike.delete()
        result = 'undislike'
    else:
        dislike = Dislikes.objects.create(post_id=post_id, user_id=u)
        dislikeCounter = Dislikes.objects.filter(post_id=post_id).count()
        if dislikeCounter == 10:
            Post.objects.get(id=post_id).delete()
            result = 'deletePost'
        else:
            result = 'dislike'
    return JsonResponse(result, safe=False)
