from django import forms

class RegisterForm(forms.Form):
  first_name = forms.CharField(max_length=45)
  last_name = forms.CharField(max_length=45)
  email = forms.EmailField()
  password1 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Password')
  password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(), label='Confirm Password')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
