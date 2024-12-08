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
            

class Transaction(CreateView, LoginRequiredMixin):
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




# class Deposit(Transaction):
#     form_class = DepositForm
#     title = "Deposit"

#     def get_inital(self):
#         DEPOSIT = TRANSACTION_TYPE[0][0]
#         initial = {"tnx_type": DEPOSIT}
#         return initial
    
#     def form_valid(self, form):
#         amount = form.cleaned_data.get('amount')
#         acount = self.request.user.acount
#         acount.balance += amount
#         acount.save(update_fields=['balance'])
#         messages.success(self.request, "DIPOSIT SUCCESSFULL")

#         return super().form_valid(form)