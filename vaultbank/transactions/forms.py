from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount", "txn_type", "approval"]


    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop("account", None)
        super().__init__(*args, **kwargs)


        #self.fields["field"].attributes  attributes["widget", "label", "required", "help_text", "inital"]
        self.fields["txn_type"].disabled = True
        self.fields["txn_type"].label = ""
        self.fields["txn_type"].widget = forms.HiddenInput()

        self.fields["approval"].disabled = True
        self.fields["approval"].label = ""
        self.fields["approval"].widget = forms.HiddenInput()


    def save(self, commit = True):
        self.instance.account = self.account
        self.instance.balance_post_txn = self.account.balance
        return super().save()

class DepositForm(TransactionForm):
    def clean_amount(self): # fitering the amount field
        min_amount = 500
        amount = self.cleaned_data.get("amount")
        if amount < min_amount:
            raise forms.ValidationError(
                f"Minimum amount to deposit is {min_amount} BDT"
            )
        return amount
    
class WithdrawForm(TransactionForm):
    def clean_amount(self):
        min_amount = 500
        max_amount = 25_000
        balance = self.account.balance
        amount = self.cleaned_data.get("amount")
        
        if amount > balance:
            raise forms.ValidationError(
                f"Amount exceeds account balance"
            )
        
        if amount < min_amount:
            raise forms.ValidationError(
                f"Minimum amount to withdraw is {min_amount} BDT"
            )
        elif amount > max_amount:
            raise forms.ValidationError(
                f"Maximum amoun to withdraw is {max_amount}"
            )

        return amount
    
class TestForm(TransactionForm):
    def clean_amount(self):
        print(self.instance.amount)
        amount = self.cleaned_data["amount"]
        if amount != 999:
            raise forms.ValidationError(
                "amount needs to be exactly 999"
            )
        return amount

class LoanForm(TransactionForm):
    def clean_amount(self):
        max_amount = self.account.balance * 2
        amount = self.cleaned_data["amount"]
        if amount > max_amount:
            raise forms.ValidationError(
                "Loan amount can be maximum of 2X of your current balance"
            )

        return amount


class PaymentForm(TransactionForm):
    pass





# testing 'how to pass kwargs between view and form'
# class TransactionSimpleForm(forms.ModelForm):
#     class Meta:
#         model = TransactionSimple
#         fields = ["amount"]
    
#     def __init__(self,*args, **kwargs):
#         self.account = kwargs.pop("account", None)
#         super().__init__(*args, **kwargs)


#     def clean_amount(self):
#         print("came here to clean amount")
#         return self.cleaned_data["amount"]
    

#     def save(self, commit = True):
#         self.instance.account = self.account
#         self.account.balance += self.cleaned_data["amount"]
#         self.account.save()
#         return super().save()
