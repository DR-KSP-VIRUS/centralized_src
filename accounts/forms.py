from django import forms
from . import models as mdl

class LoginForm(forms.Form):
    email = forms.CharField(label="Email",required=True,widget=forms.TextInput(attrs={
        'class':"form-control",
        'placeholder': 'Enter email...' 
    }))

    password = forms.CharField(label="Password",required=True,widget=forms.PasswordInput(attrs={
        'class':"form-control",
        'placeholder': 'Password...'
    }))

class PortfolioForm(forms.ModelForm):
    
    class Meta:
        model = mdl.Portfolio
        fields = ("full_name","title", "first_phone","second_phone","email","photo","turnor")
        widgets = {
            'full_name':forms.TextInput(attrs={
                'class':"form-control",
                'placeholder': 'e.g Konja Kuma Sampson',
                'required':True, 'autofocus':True
            }),
            'title':forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'src president',
                'required':True
            }),
            'first_phone':forms.TextInput(attrs={
                'class':"form-control",
                'placeholder': 'e.g 0541424847',
                'required':True,
            }),

            'first_phone':forms.TextInput(attrs={
                'class':"form-control",
                'placeholder': 'e.g 0541424847',
                'required':True,
            }),

            'second_phone':forms.TextInput(attrs={
                'class':"form-control",
                'placeholder': 'e.g 0508450222',
                'required':True,
            }),

            'email':forms.EmailInput(attrs={
                'class':"form-control",
                'placeholder': 'e.g example@gmail.com',
                'required':True,
            }),

            'photo':forms.ClearableFileInput(attrs={
                'class':"form-control",
                'placeholder': 'e.g 0541424847',
                'required':True,
            }),
            'turnor':forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'e.g 2024/2025',
                'required':True
            })
        }