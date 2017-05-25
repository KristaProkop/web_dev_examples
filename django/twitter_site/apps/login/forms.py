from django import forms

class RegisterForm(forms.Form):
  handle = forms.CharField(max_length=100, label="Twitter Handle")
  password1 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Password')
  password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(), label='Confirm Password')

class LoginForm(forms.Form):
    handle = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
