from django import forms
from pyapp.models import Post,Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'picture', 'content','created_date','category')
