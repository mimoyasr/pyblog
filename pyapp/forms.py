from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class UniqueUserEmailField(forms.EmailField):
    """
    An EmailField which only is valid if no User has that email.
    """
    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        try:
            User.objects.get(email = value)
            raise forms.ValidationError("Email already exists")
        except User.MultipleObjectsReturned:
            raise forms.ValidationError("Email already exists")
        except User.DoesNotExist:
			pass



class SignUpForm(UserCreationForm):
    email = UniqueUserEmailField(required = True, label = 'Email address')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
"""""

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'created_date', 'post_id', 'user_id')
"""

