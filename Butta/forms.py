from dataclasses import fields
from django import forms
from Butta.models import Customer, Product, Order, Contact_us


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = "__all__"
