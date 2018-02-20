from django import forms
from pyapp.models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('cat_name',)

class BadWordsForm(forms.ModelForm):
    class Meta:
        model = BadWords
        fields = ('word',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'picture', 'content' ,'category')

