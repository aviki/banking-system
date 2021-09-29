from django.shortcuts import render, get_object_or_404
from .models import Customer, Account
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import CreateNewCustomer
# Create your views here.

@login_required
def index(request):
    customer = Customer.objects.filter(user=request.user)
    account = Account.objects.all()
    context = {
            'customer': customer,
            'account': account
        }


    return render(request, 'bank_app/index.html', context)


def create(response):
    form = CreateNewCustomer()
    return render(response, 'bank_app/create.html', {"form":form})
