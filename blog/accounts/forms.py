from user.models import Post,User_details,Comment
from django.forms import ModelForm
from django import forms


class User_detailForm(forms.ModelForm):
    class Meta:
        model=User_details
        fields=['username','f_name','l_name','email','password','phone_no','profile_img']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your username', 'autocomplete': 'off'}),
            'f_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your first name'}),
            'l_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your last name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your email'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your password', 'autocomplete': 'off'}),
            'phone_no': forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Phone No','autocomplete': 'off'}),
            'profile_img': forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Add Your profile Picture'})

        }