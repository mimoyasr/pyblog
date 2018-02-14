# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from pyapp.forms import SignUpForm

# Create your views here.

def login_form(request):

    if request.method == 'POST':

        name = request.POST['username']
        password = request.POST['password']
	
	#authenticate first search for the user in database and if found
	#it returns user object
	#and if it didn't find a user it will return None
        user = authenticate(username=name,password=password)

        if user is not None: #this means we found the user in database
            login(request,user)#this means we put the user id in the session

            return HttpResponse('logged in succes')



    return render(request,'login_form.html')

#this is a decorator
#https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-login-required-decorator
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