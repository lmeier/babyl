from django import forms
from django.contrib.auth.models import User
from .models import Post, Blog
from django.template.defaultfilters import slugify

# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('username', 'email')

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')


class NewBabylForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        super(NewBabylForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
    
    def __init__(self, *args, **kwargs):
        super(NewPostForm, self).__init__(*args, **kwargs)