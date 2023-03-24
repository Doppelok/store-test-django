from django import forms
from multi_store.models import UserShoppingCart
from .models import CheckoutOrder


class ShoppingCartForm(forms.ModelForm):
    quantity = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-sm bg-secondary border-0 text-center', 'value': 'cart.quantity'
    }))

    class Meta:
        model = UserShoppingCart
        fields = ['quantity']


class CheckOutForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'type': 'text', 'placeholder': 'Your name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'type': 'text', 'placeholder': 'Your last name'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'type': 'text', 'placeholder': 'example@email.com'
    }))

    mobile_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'type': 'text', 'placeholder': '+380 96 22 55 888'
    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'type': 'text', 'placeholder': '123 Street'
    }))

    country = forms.ChoiceField(choices=CheckoutOrder.COUNTRY, widget=forms.Select(attrs={
        'class': 'form-control', 'type': 'text'
    }))

    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'type': 'text', 'placeholder': 'Kyiv'
    }))

    state = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'type': 'text', 'placeholder': 'Kyiv'
    }))

    zip_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'type': 'text', 'placeholder': '80056'
    }))

    class Meta:
        model = CheckoutOrder
        fields = [
            'first_name',
            'last_name',
            'email',
            'mobile_no',
            'address',
            'country',
            'city',
            'state',
            'zip_code',
        ]
