# main_app/forms.py
from django import forms
from .models import Cat


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'breed', 'description', 'age']


class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())


    # name = forms.CharField(label='Name', max_length=100)
    # breed = forms.CharField(label='Breed', max_length=100)
    # description = forms.CharField(label='Description', max_length=250)
	# 	age = forms.IntegerField(label='Age')
