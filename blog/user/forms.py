from user.models import Post
from django.forms import ModelForm
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['image','description']
        widgets={
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'description'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Add Your profile Picture'})
        }