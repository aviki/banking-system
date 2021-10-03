from django.shortcuts import render, get_object_or_404
from .models import Customer, Account, Ledger, Uid, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import CreateNewCustomer, CreateNewAccount, MakeTransfer
from django.db import transaction
# Create your views here.

@login_required
def index(request):
    customer = Customer.objects.filter(user=request.user)
    accounts = Account.objects.filter(user=request.user)
    context = {
            'customer': customer,
            'accounts': accounts
            }


    return render(request, 'bank_app/index.html', context)


def create(response):
    customer_form = CreateNewCustomer()

    context = {
        'customer_form':customer_form,
           }
    return render(response, 'bank_app/create.html', context)

def createaccount(request):

    if request.method=="POST":
        customer_id = request.POST["customer_id"]
        account = Account()
        account.save()
    account_form = CreateNewAccount()

    context = {
        'account_form':account_form,
            }

    return render(request, 'bank_app/create_account.html', context)

def details(request, pk):
    account_number = Account.objects.get(pk=pk)
    transactions = Ledger.objects.filter(account=account_number).order_by('-transaction_date')
    context = {
        'account_number':account_number,
        'transactions':transactions,
            }
    return render(request, 'bank_app/details.html', context)

def transfer(request):
    if request.method=="POST":
        with transaction.atomic():
            from_account = request.POST['from_account']
            if Account.objects.get(account_number=from_account):
                to_account = request.POST['to_account']
                if Account.objects.filter(account_number=to_account):
                    amount = int(request.POST['amount'])
                    uid = Uid()
                    uid.save()
                    Ledger.objects.create(account=Account.objects.get(account_number=from_account), transaction=amount*-1, ref=Uid.objects.last())
                    Ledger.objects.create(account=Account.objects.get(account_number=to_account), transaction=amount, ref=Uid.objects.last())
  #accounts = Account.objects.filter(user=request.user)
  #accounts_numbers=accounts.values_list('account_number')
    transfer_form = MakeTransfer()
    context = {
        'transfer_form':transfer_form,
    #    'accounts':accounts,
     #   'accounts_numbers':accounts_numbers,
          }

    return render(request, 'bank_app/transfer.html', context)

