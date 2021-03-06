from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from pyapp.models import Category, BadWords, Post
from .forms import *
from pyapp.forms import SignUpForm


def allUsers(request):
    all_users = User.objects.all()
    context = {"allusers": all_users}
    return render(request, "users_tables.html", context)


def user_block(request, usr_id):
    usr = User.objects.get(id=usr_id)
    usr.is_active = 0
    usr.save()
    return HttpResponseRedirect("/allusers")


def user_promote(request, usr_id):
    usr = User.objects.get(id=usr_id)
    usr.is_superuser = 1
    usr.save()
    return HttpResponseRedirect("/allusers")


def user_unblock(request, usr_id):
    usr = User.objects.get(id=usr_id)
    usr.is_active = 1
    usr.save()
    return HttpResponseRedirect("/allusers")


def user_delete(request, usr_id):
    usr = User.objects.get(id=usr_id)
    usr.delete()

    return HttpResponseRedirect("/allusers")


def user_update(request, usr_id):
    usr = User.objects.get(id=usr_id)
    form = SignUpForm(instance=usr)
    if request.method == "POST":
        form = SignUpForm(request.POST, instance=usr)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allusers")
    context = {"form": form}
    return render(request, "signup.html", context)


def user_new(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allusers")
    context = {"form": form}
    return render(request, "signup.html", context)


def allCategories(request):
    all_categories = Category.objects.all()
    context = {"allcategories": all_categories}
    return render(request, "categories_tables.html", context)


def allTags(request):
    all_tags = Tag.objects.all()
    context = {"all_tags": all_tags}
    return render(request, "tags_tables.html", context)

def category_new(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allcategories")
    context = {"form": form}
    return render(request, "newcategory.html", context)


def tag_new(request):
    form = TagForm()
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/alltags")
    context = {"form": form}
    return render(request, "newtag.html", context)

def category_update(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    form = CategoryForm(instance=cat)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allcategories")
    context = {"form": form}
    return render(request, "newcategory.html", context)


def category_delete(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    cat.delete()
    return HttpResponseRedirect("/allcategories")


def allBadwords(request):
    all_badwords = BadWords.objects.all()
    context = {"allbadwords": all_badwords}
    return render(request, "forbiddenwords_tables.html", context)


def badword_new(request):
    form = BadWordsForm()
    if request.method == "POST":
        form = BadWordsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allbadwords")
    context = {"form": form}
    return render(request, "newbadword.html", context)


def badword_update(request, word_id):
    badword = BadWords.objects.get(id=word_id)
    form = BadWordsForm(instance=badword)
    if request.method == "POST":
        form = BadWordsForm(request.POST, instance=badword)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allbadwords")
    context = {"form": form}
    return render(request, "newbadword.html", context)


def badword_delete(request, word_id):
    badword = BadWords.objects.get(id=word_id)
    badword.delete()

    return HttpResponseRedirect("/allbadwords")


def allPosts(request):
    all_posts = Post.objects.order_by('-created_date')
    context = {'all_posts': all_posts}
    return render(request, 'posts_tables.html', context)


def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/allposts')
    return render(request, 'post.html', {'form': form})

def getPost(request, post_id):
    post = Post.objects.get(id = post_id)
    commentscount=Comment.objects.filter(post=post_id).count()
    likescount=Likes.objects.filter(post=post_id).count()
    dislikescount=Dislikes.objects.filter(post=post_id).count()
    context = {"post":post,"commentscount":commentscount,"likescount":likescount,"dislikescount":dislikescount }
    return render(request, "post_details.html", context)






def Posts_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/allposts')
    else:
        form = PostForm(instance=post)
    return render(request, 'post.html', {'form': form})


def Post_delete(request, post_id):
    obj = Post.objects.get(id=post_id)
    obj.delete()
    return HttpResponseRedirect('/allposts')


def admin(request):
    postscount = Post.objects.all().count()
    userscount = User.objects.all().count()
    catscount = Category.objects.all().count()
    wordscount = BadWords.objects.all().count()
    context = {'postcount': postscount, 'usercount': userscount, 'catcount': catscount, 'wordcount': wordscount}
    return render(request, 'index.html', context)
