from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    birth_date 	= forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    location 	= forms.CharField(max_length=100)
    bio 		= forms.CharField(widget=forms.Textarea)
    image 		= forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','birth_date','bio','image','location','password1', 'password2',)
