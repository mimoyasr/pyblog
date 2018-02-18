from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from pyapp.models import Category,BadWords
from .forms import CategoryForm,BadWordsForm

def allUsers(request):
  all_users=User.objects.all()
  context={"allusers":all_users}
  return render(request,"users.html",context)

def user_block(request,usr_id):
    usr=User.objects.get(id=usr_id)
    usr.is_active=0
    usr.save()
    return HttpResponseRedirect("/allusers")

def user_promote(request,usr_id):
    usr=User.objects.get(id=usr_id)
    usr.is_superuser=1
    usr.save()
    return HttpResponseRedirect("/allusers")

def user_unblock(request,usr_id):
    usr=User.objects.get(id=usr_id)
    usr.is_active=1
    usr.save()
    return HttpResponseRedirect("/allusers")


def allCategories(request):
  all_categories=Category.objects.all()
  context={"allcategories":all_categories}
  return render(request,"categories.html",context)

def category_new(request):
    form=CategoryForm()
    if request.method == "POST":
        form= CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allcategories")
    context={"form":form}
    return render(request,"newcategory.html",context)

def category_update(request,cat_id):
    cat=Category.objects.get(id=cat_id)
    form = CategoryForm( instance=cat)
    if request.method == "POST":
        form= CategoryForm(request.POST,instance=cat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allcategories")
    context={"form":form}
    return render(request,"newcategory.html",context)


def category_delete(request,cat_id):
    cat=Category.objects.get(id=cat_id)
    cat.delete()

    return HttpResponseRedirect("/allcategories")


def allBadwords(request):
  all_badwords=BadWords.objects.all()
  context={"allbadwords":all_badwords}
  return render(request,"badwords.html",context)

def badword_new(request):
    form=BadWordsForm()
    if request.method == "POST":
        form= BadWordsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allbadwords")
    context={"form":form}
    return render(request,"newbadword.html",context)

def badword_update(request,word_id):
    badword=BadWords.objects.get(id=word_id)
    form = BadWordsForm( instance=badword)
    if request.method == "POST":
        form= BadWordsForm(request.POST,instance=badword)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allbadwords")
    context={"form":form}
    return render(request,"newbadword.html",context)


def badword_delete(request,word_id):
    badword=BadWords.objects.get(id=word_id)
    badword.delete()

    return HttpResponseRedirect("/allbadwords")




