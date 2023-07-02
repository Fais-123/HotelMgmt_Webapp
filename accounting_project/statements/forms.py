from django import forms
from .models import Transaction,Account



class TransactionForm(forms.Form):
    account1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    account2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    credit_amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    debit_amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
