from django import forms
from .models import Customer, Account
from django.core.validators import RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError

class CreateNewCustomer(forms.Form):
    firstName = forms.CharField(label="First Name", max_length=200)
    lastName = forms.CharField(label="Last Name", max_length=200)
    email = forms.EmailField(label="Email")

    rank = forms.ChoiceField(choices=Customer.RANK_CHOICES, widget=forms.RadioSelect)

class CreateNewAccount(forms.Form):
    customer_id = forms.IntegerField(label="Customer ID")


class MakeTransfer(forms.Form):
        from_account = forms.CharField(label='From account', max_length=200)
        to_account = forms.CharField(label='To account', max_length=200)
        amount = forms.DecimalField(label='amount', decimal_places=2, max_digits=12, min_value='0.01')
