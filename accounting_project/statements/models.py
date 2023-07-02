from django.db import models

# Create your models here.

from django.db import models

class Account(models.Model):
    credit_account = models.CharField(max_length=100,default='service revenue')
    debit_account = models.CharField(max_length=100,default='utility expense')
    account_type = models.CharField(max_length=100, default='GL_account')

    def __str__(self):
        return self.account_type

class Transaction(models.Model):

    account1 = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='credit')
    account2 = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='debit')
    credit_amount = models.IntegerField()
    debit_amount = models.IntegerField()
    date = models.DateField()

    # def __str__(self):
    #     return f"Transaction: {self.account} - {self.amount}"
