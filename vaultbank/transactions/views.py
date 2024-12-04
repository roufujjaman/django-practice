from django.shortcuts import render
from .forms import TransactionForm
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, TRANSACTION_TYPE
# from .forms import DepositForm, WithdrawForm
from django.contrib import messages


from django.db.utils import IntegrityError


#testing
from .forms import TransactionForm, TransactionSimpleForm

def test(request):
    form = TransactionSimpleForm() 
    
    if request.method == "POST":
        form = TransactionSimpleForm(request.POST, account=request.user.account)
        if form.is_valid():
            form.save()

    return render(request, 'transactions/transaction_form.html', 
                  {"TransactionForm": form})


# class Transaction(CreateView, LoginRequiredMixin):
#     template_name = "transaction/transaction_form.html"
#     model = Transaction
#     title = None
#     success_url = ""

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         kwargs.update(
#             {"title": self.title}
#         )
#         return context
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update(
#             {'account': self.request.user.account}
#         )
#         return kwargs
    

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