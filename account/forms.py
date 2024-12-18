from .models import User
from django import forms

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))

# forms.py
class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'}))


class RegisterForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone', 'password']





