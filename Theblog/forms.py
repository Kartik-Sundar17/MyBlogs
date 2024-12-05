from django import forms
from .models import Post,Comment

# PostForms for creating and editing posts
class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'content', 'snippet', 'cat', 'img')
        

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'cat': forms.Select(attrs={'class': 'form-control'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add Quotation To Appear Below Post Content'}),
        }

# EditForms for editing existing posts
class EditForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',  'content', 'snippet', 'img')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            #'cat': forms.Select(attrs={'class': 'form-control'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Add 'cat', 'title_tag' in fields if required

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            
        }