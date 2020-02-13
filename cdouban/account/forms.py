from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomerForm(UserCreationForm):
    """docstring for CustomerForm."""
    nickname = forms.CharField(max_length=50, required=False, label ='昵称')
    birthday = forms.DateField(required=False, label='生日')
    location = forms.CharField(required=True, label='常住地')
    avartar = forms.ImageField(required=False, label='头像')
    

    class Meta:
        model = User
        fields = ('username', 'nickname', 'avartar', 'password1','password2', 'email', 'birthday', 'location')
