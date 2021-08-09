from django.contrib.auth import get_user_model

from django import forms

from .models import Profile

class ProfileEditForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('date_of_birth', 'photo')

