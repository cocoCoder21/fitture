from django import forms
from fitapp.models import UserModels
from django.contrib.auth.models import User


class UserInfoForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'password',  'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        for feild in ['username',  'first_name', 'last_name', 'password']:
            self.fields[feild].help_text = None


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserModels
        fields = ('email', 'gender', 'country', 'birth_date')
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'required': True, 'placeholder': 'Enter Email'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter Country'})
        }
