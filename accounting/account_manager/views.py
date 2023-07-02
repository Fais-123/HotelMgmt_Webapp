from django.shortcuts import render
from .logic import generate_income_statement, generate_balance_sheet

# Create your views here.


def income_statement(request):
    output, expenses, net_income = generate_income_statement()

    # revenue, expenses, net_income = generate_income_statement()
    # return render(request, 'income_statement.html', {'revenue': revenue, 'expenses': expenses, 'net_income': net_income})
    return render(request, 'income_statement.html', {'output': output, 'expenses': expenses, 'net_income': net_income})

def balance_sheet(request):
    balances, total_assets, total_liabilities, total_equity = generate_balance_sheet()
    return render(request, 'balance_sheet.html', {'balances': balances, 'total_assets': total_assets, 'total_liabilities': total_liabilities, 'total_equity': total_equity})
