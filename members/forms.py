from django import forms
from django.contrib.auth.models import User
from Theblog.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'insta_url', 'twitter_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'insta_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '150',
                'pattern': '[A-Za-z\s]+',
                'required': 'required'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '150',
                'pattern': '[A-Za-z\s]+',
                'required': 'required'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '150',
                'pattern': '[a-zA-Z0-9@.+-_]+',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
        }
