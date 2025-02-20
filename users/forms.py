from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterUserForm(forms.ModelForm):

    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    apartment_name = forms.CharField(label='Apartment Name')
    apartment_number = forms.CharField(label='Apartment No')
    phone_number = forms.IntegerField()
    
    class Meta:
        model = User
        fields ={'username','email','first_name'}

    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data['password2']
    
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'first_name','last_name','email'}

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields ={'image','apartment_name','apartment_number','phone_number'}

