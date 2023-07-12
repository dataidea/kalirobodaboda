from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    username = forms.CharField(max_length=25)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
