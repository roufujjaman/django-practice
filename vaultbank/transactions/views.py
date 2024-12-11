from django.shortcuts import render
from .forms import TransactionForm
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, TRANSACTION_TYPE
from . import forms
from django.contrib import messages


def transaction(request):
    form = TransactionForm()
    
    if request.method == "POST":
        form = TransactionForm(request.POST, account=request.user.account)

        form.initial["txn_type"] = 1

        if form.is_valid():

            amount = form.cleaned_data["amount"]
            account = request.user.account
            account.balance += amount
            account.save(update_fields=["balance"])
            form.save()

    return render(request, 'transactions/transaction_form.html', 
                  {"TransactionForm": form,
                   "subtitle": "Deposit"})
            




class Transaction(LoginRequiredMixin, CreateView):
    login_url = "/account/login"
    model = Transaction
    template_name = 'transactions/transaction_form.html'
    success_url = '/account'


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            kwargs.update(
                {"account": self.request.user.account}
            )
        return kwargs


def test(request):
    return render(request,'transactions/transaction_form.html' )



class Test(Transaction):
    form_class= forms.TestForm
    title = "Test"
    initial = {"txn_type": 3}

    def form_valid(self, form):


        print(form.instance.amount)
        print(form.instance.txn_type)
        print(form.instance.created_at)
        print(form.instance.approval)
        print(form.instance.account)
        

    
        return super().form_valid(form)


class DepositView(Transaction):
    form_class = forms.DepositForm
    title =  "Deposit"
    initial = {"txn_type": 1}
    
    
    extra_context = {
        "subtitle": "Deposit",
    }

    def form_valid(self, form):
        amount = form.cleaned_data["amount"]
        account = self.request.user.account
        account.balance += amount

        account.save(
            update_fields = ["balance"]
        )

        return super().form_valid(form)

class WithdrawView(Transaction):
    form_class = forms.WithdrawForm
    initial = {"txn_type": 2}
    extra_context = {
        "subtitle": "Withdraw"
    }

    def form_valid(self, form):
        amount = form.cleaned_data["amount"]
        account = self.request.user.account
        account.balance -= amount

        account.save(
            update_fields=["balance"]
        )

        return super().form_valid(form)


class LoanView(Transaction):
    pass 