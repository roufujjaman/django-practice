from django.shortcuts import render
from .forms import TransactionForm
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, TRANSACTION_TYPE
from . import forms
from django.views.generic import ListView


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
            




class TransactionView(LoginRequiredMixin, CreateView):
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

class DepositView(TransactionView):
    form_class = forms.DepositForm
    title =  "Deposit"
    initial = {"txn_type": 1, "approval": True}
    
    
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

class WithdrawView(TransactionView):
    form_class = forms.WithdrawForm
    initial = {"txn_type": 2, "approval": True}
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


class LoanRequestView(TransactionView):
    form_class = forms.LoanForm
    initial = {"txn_type": 3}
    extra_context = {
        "subtitle": "Loan Request"
    }

    def form_valid(self, form):
        amount = form.cleaned_data["amount"]
        account = self.request.user.account
        account.balance += amount

        account.save(
            update_fields=["balance"]
        )

        return super().form_valid(form)
    
class LoansView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "transactions\loan_list.html"
    context_object_name = "loanlist"

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account= self.request.user.account,
            txn_type=3
        ).order_by("-created_at")

        pay_id = self.request.GET.get("id")

        print(pay_id)

        return queryset