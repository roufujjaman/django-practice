from django.forms import ModelForm
from .models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'txn_type']

    
    # def __init__(self, *args, **kwargs):
    #     self.account = kwargs.pop(account)
    #     super.__init__(*args, **kwargs)
    #     return