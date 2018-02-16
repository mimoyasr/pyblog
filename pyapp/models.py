# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib.auth.models import User


class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    content = models.TextField(max_length=400)
    category = models.ForeignKey(Category)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Badwords(models.Model):
    word = models.CharField(max_length=200)
    def __str__(self):
        return self.word


class Comment(models.Model):
    text = models.TextField(max_length=400)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    def __str__(self):
        return self.text


class Likes(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)


class Dislikes(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)


class Reply(models.Model):
    text = models.TextField(max_length=400)
    created_date = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    comment = models.ForeignKey(Comment)
    def __str__(self):
        return self.text


class Tag(models.Model):
    tag = models.CharField(max_length=200)


class Post_tag(models.Model):
    tag = models.ForeignKey(Tag)
    post = models.ForeignKey(Post)
