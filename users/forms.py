from django import forms

class UserForms(forms.Form):
    name = forms.CharField(max_length=200, label='name')
    surname = forms.CharField(max_length=200, label='surname')
    gender = forms.CharField(max_length=200, label='gender')
    adult = forms.BooleanField(label='adult')