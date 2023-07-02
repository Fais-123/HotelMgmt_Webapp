from django.db import models
from django.contrib.auth.models import User


class Accounts(models.Model):
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    balance = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
class Transactions(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=100)
    amount = models.IntegerField()
    account_id = models.ForeignKey('Accounts', on_delete=models.CASCADE)

class Entries(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=100)
    debit_account_id = models.ForeignKey('Accounts', related_name='debit_ledger_entries', on_delete=models.CASCADE)
    debit_amount = models.IntegerField()
    credit_account_id = models.ForeignKey('Accounts', related_name='credit_ledger_entries', on_delete=models.CASCADE)
    credit_amount = models.IntegerField()
