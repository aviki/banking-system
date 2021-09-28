from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.db.models import Sum

class Account(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
 #   account_number = models.ChatField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    account_number = models.UUIDField(default=uuid.uuid4, editable=False)


    @property
    def balance(self):
        return Ledger.objects.filter(account=self).aggregate(Sum('transaction'))

class Uid(models.Model):
    pass

class Ledger(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction = models.DecimalField(decimal_places=2, max_digits=12)
    ref = models.ForeignKey(Uid, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()

# Create your models here.
