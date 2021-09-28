from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = PhoneNumberField()
    RANK_CHOICES = [('G', 'Gold'), ('S', 'Silver'), ('B', 'Basic')]
    rank = models.CharField(max_lenght=1, choices=RANK_CHOICES, blank=False)

# Create your models here.
