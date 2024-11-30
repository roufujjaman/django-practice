from django.shortcuts import render
from .forms import TransactionForm
# Create your views here.
def home(request):
    return render(request, "transactions/transaction_form.html", {
        "TransactionForm": TransactionForm
    })