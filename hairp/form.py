from typing import Any, Dict
from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm
from django.contrib.auth.models import User

class sig(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class sig1(SetPasswordForm):
    class Meta:
        model=User
        fields=['username','new_password1','new_password2']

class sig2(UserCreationForm):
    class Meta:
        model=User
        fields='__all__'