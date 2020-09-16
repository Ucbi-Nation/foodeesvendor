from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from .models import UserProfile


class ImageUpdate(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image',)
        widgets = {
            'image'     : FileInput(attrs={'class': 'imgInp', 'id': 'imgInp', 'label':'ddd','placeholder': 'imsssage', }),
        }

