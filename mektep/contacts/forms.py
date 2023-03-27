from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
#mektep4

class SignUpForm(UserCreationForm):
    class Meta:
        model = CUser
        fields = ('first_name','last_name','username','email', 'password1', 'password2', )


class ProfileChange(forms.ModelForm):
    class Meta:
        m = "Мужчина"
        w = "Женщина"
        other = "Другой"
        gender_choices = ((m,"Мужчина"),
                        (m,"Женщина"),
                        (other,"Другой"))
        model = CUser
        fields = ('first_name','last_name','username','city','country',
                  'birthday','gender','face','interes')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'interes':forms.Textarea(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'face':forms.FileInput(attrs={'class':'form-control'}),
            'gender':forms.Select( attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
