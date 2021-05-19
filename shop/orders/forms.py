from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'city', 'postal_code', 'address']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'city': 'Город',
            'postal_code': 'Индекс',
            'address': 'Адрес',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше имя"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваша фамилия"}),
            'email': forms.TextInput(attrs={"class": "form-control", "placeholder": "Адрес электронной почты"}),
            'city': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваш город"}),
            'postal_code': forms.TextInput(attrs={"class": "form-control", "placeholder": "Индекс"}),
            'address': forms.TextInput(attrs={"class": "form-control", "placeholder": "Адрес доставки"}),
        }
