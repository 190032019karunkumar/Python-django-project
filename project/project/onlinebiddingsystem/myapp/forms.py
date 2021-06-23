from .models import Bid,Test
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password1', 'password2']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = "__all__"

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__"