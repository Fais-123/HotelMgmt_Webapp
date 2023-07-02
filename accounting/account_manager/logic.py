from django.db.models import Sum
from .models import Transaction, Account

def generate_income_statement():
    accounts = Account.objects.filter(account_type__icontains="revenue")
    expenses = Account.objects.filter(account_type__icontains="expense")
    # print('accounts',accounts)
    # print('expenses',expenses)
  

    

# def generate_income_statement():
#     accounts = Account.objects.filter(account_type__icontains="revenue")
#     expenses = Account.objects.filter(account_type__icontains="expense")
#     # print('accounts',accounts)
#     # print('expenses',expenses)
  

#     for i in accounts:
#         revenue = Transaction.objects.filter(account=i).aggregate(total_income=Sum('amount'))
#         rev = 0
#         # for i in revenue:
#         output = sum(revenue.values())
#             # revs=[]
#             # rev = revenue[i]
#             # revs = revs.append(rev)
#             # print(type(revs))
#             # output = sum(revs)
#         print(output) 

#     for i in expenses:
#         expenses = Transaction.objects.filter(account=i).aggregate(total_expenses=Sum('amount'))
#         exp = 0
#         for i in expenses:
#             exp = expenses[i] + exp
#         # print(exp)

   
#     net_income = revenue['total_income'] - expenses['total_expenses']

#     # return revenue, expenses, net_income
#     return output, expenses, net_income


def generate_balance_sheet():
    accounts = Account.objects.all()
    balances = {}
    total_assets = 0
    total_liabilities = 0
    total_equity = 0

    for account in accounts:
        balance = Transaction.objects.filter(account=account).aggregate(total_balance=Sum('amount'))
        balances[account] = balance['total_balance']
        if balance['total_balance'] > 0:
            total_assets += balance['total_balance']
        elif balance['total_balance'] < 0:
            total_liabilities += balance['total_balance']
        else:
            total_equity += balance['total_balance']

    return balances, total_assets, total_liabilities, total_equity
