from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.db.models import Sum
from django.db.models.functions import Coalesce


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    phone = PhoneNumberField()
    RANK_CHOICES = [('G', 'Gold'), ('S', 'Silver'), ('B', 'Basic')]
#    rank = models.CharField(max_length=1, choices=RANK_CHOICES, blank=False)
    def __str__(self):
        return f"{self.user}"

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 #   account_number = models.ChatField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    account_number = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    def __str__(self):
        return f"{self.account_number}"

    @property
    def balance(self):
        #if Ledger.objects.filter(account=self).aggregate(Sum('transaction'))
    #rows = Ledger.objects.filter(account=self)
   # total_balance = rows.aggregate(Sum('transaction')) if rows else 0
        return Ledger.objects.filter(account=self).aggregate((Sum('transaction'))) if Ledger.objects.filter(account=self) else 0
     #    return Ledger.objects.filter(account=self).annotate(total=Coalesce(Sum('transaction'), 0))
    #    return total_balance

class Uid(models.Model):
    pass

class Ledger(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction = models.DecimalField(decimal_places=2, max_digits=12)
    ref = models.ForeignKey(Uid, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()


# Create your models here.
