from django import forms
from django.db import transaction
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

class SignupForm(forms.ModelForm):
    password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter atleast 6 charaters'
    }))
    password1 = forms.CharField(label='Confirm Password',max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm Password'
    }))
    class Meta:
        model = mdl.User
        fields = ('email',)
        widgets = {
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Enter active email...',
            })
        }

    def cleaned_password(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if(password and password1) and (password1 == password):
            return password1
        raise forms.ValidationError('Passwords do not match')
    
    @transaction.atomic
    def save(self, commit: bool = False):
        user = super().save(commit)
        user.email = self.cleaned_data.get('email')
        user.full_name = self.cleaned_data.get('full_name')
        user.set_password(self.cleaned_password())
        user.student = True
        user.save()
        return user

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
                'required':False,
            }),
            'turnor':forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'e.g 2024/2025',
                'required':True
            })
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = mdl.Profile
        fields = ('full_name', 'phone','gender','image')
        widgets = {
            'full_name':forms.TextInput(attrs={
                'class':'form-control',
                'autofocus':True
            }),
            'phone':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'gender':forms.Select(attrs={
                'class':'form-control'
            }),
            'image':forms.ClearableFileInput(attrs={
                'class':'form-control'
            })
        }