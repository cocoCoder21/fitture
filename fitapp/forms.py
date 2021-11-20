from django import forms
from fitapp.models import  UserModels
from django.contrib.auth.models import User

class UserInfoForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username',  'first_name','last_name', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            # 'email': forms.EmailInput(attrs={'required': True}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserModels
        fields = ('email', 'gender', 'country', 'birth_date')
        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'}),
            'email': forms.EmailInput(attrs={'required': True}),
        }
