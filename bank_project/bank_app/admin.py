from django.contrib import admin
from .models import Account, Customer, Ledger, Uid


admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Ledger)
admin.site.register(Uid)

# Register your models here.
