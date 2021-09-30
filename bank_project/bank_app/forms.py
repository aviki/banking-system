from django import forms
from .models import Customer, Account
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class CreateNewCustomer(forms.Form):
    firstName = forms.CharField(label="First Name", max_length=200)
    lastName = forms.CharField(label="Last Name", max_length=200)
    email = forms.EmailField(label="Email")

    rank = forms.ChoiceField(choices=Customer.RANK_CHOICES, widget=forms.RadioSelect)

class CreateNewAccount(forms.Form):
    customer_id = forms.IntegerField(label="Customer ID")
