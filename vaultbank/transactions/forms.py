from django.forms import ModelForm, HiddenInput, ValidationError
from .models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'txn_type']

    
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super.__init__(*args, **kwargs)
        self.fields['tnx_type'].disabled = True
        self.fields['tnx.type'].widget = HiddenInput()


    def save(self, commit = True):
        self.instance.account = self.account
        self.instance.balance_post_tnx = self.account.balance
        return super().save()

class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise ValidationError("The amount needs to be bigget than 100")
        
        else:
            return amount

# class WithdrawForm(Transaction):
#     def clea_amount(self):
#         account = self.account
#         min_withdraw_amount = 500
#         max_withdraw_amount = 20_000
#         balance = account.balance
#         amount = self.clean_date.get("amount")
#         if not(min_withdraw_amount <= amount <= max_withdraw_amount):
#             raise ValidationError(f"The amount needs to be between {min_withdraw_amount} & {max_withdraw_amount}")
#         elif amount < balance:
#             raise ValidationError("Insufficient Balance")
#         else:
#             return amount