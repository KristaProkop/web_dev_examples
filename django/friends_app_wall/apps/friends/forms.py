from django import forms
from .models import User, UserProfile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email' ]

class EditProfileImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']