from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from homevibe.models import User


class SigninForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets={
            'username':forms.EmailInput(),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }
# helptext
