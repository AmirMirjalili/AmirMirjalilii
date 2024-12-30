from django import forms
from .models import Provence, City, Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'province', 'city']

    province = forms.ModelChoiceField(
        queryset=Provence.objects.all(),
        label="Province",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'province-select'})
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.none(),
        label="City",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'city-select'})
    )
