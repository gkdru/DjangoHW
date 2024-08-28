from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    cv = forms.FileField(label='Cv')
    photo = forms.ImageField(label='photo')
    id_photo = forms.ImageField(label='id photo')


    class Meta:
        model = UserProfile
        fields = '__all__'
        

