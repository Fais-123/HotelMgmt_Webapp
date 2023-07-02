from django.shortcuts import render,redirect
from .models import Accounts,Transactions,Entries
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def account(request):
    if request.method == 'POST':
        name = request.POST['name']
        account_type = request.POST['account_type']
        balance = request.POST['balance']
        username = request.POST['user']
        try:
            # Retrieve the user object or create it
            # a tuple user holds username, created hold status if created True otherwise False.
            user, created = User.objects.get_or_create(username=username)
            
            # Create the account object
            account = Accounts(name=name, account_type=account_type, balance=balance, user=user)
            account.save()
            
            # Redirect to a success page or desired URL
            return redirect('success')
        
        except Exception as e:
            # Handle any exceptions that occur during account creation
            messages.error(request, str(e))
            return redirect('account')
    return render(request,'account.html')


def create_transaction(request):
    accounts = Accounts.objects.all()
    print('accounts',accounts)
    if request.method == 'POST':
        date = request.POST['date']
        description = request.POST['description']
        amount = request.POST['amount']
        account_id = request.POST['account_id']

        try:
            account = Accounts.objects.get(id=account_id) #get account with specified id if exist
            print('account',account)
        except Accounts.DoesNotExist:
            # Handle the case where the specified account_id does not exist
            return render(request, 'error.html', {'message': 'Account does not exist'})

        # Create the transaction instance and save it
        transaction = Transactions(date=date, description=description, amount=amount, account_id=account)
        transaction.save()

        return redirect('success') # Redirect to transaction list page

    return render(request, 'transaction.html',{'accounts':accounts})

def save_entries(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        description = request.POST.get('description')
        debit_account_id = request.POST.get('debit_account_id')
        debit_amount = request.POST.get('debit_amount')
        credit_account_id = request.POST.get('credit_account_id')
        credit_amount = request.POST.get('credit_amount')

        # Retrieve the Accounts instances based on the account IDs
        try:
            debit_account = Accounts.objects.get(id=debit_account_id)
            credit_account = Accounts.objects.get(id=credit_account_id)

        except Accounts.DoesNotExist:
            # Handle the case where the specified account IDs do not exist
            return render(request, 'error.html', {'message': 'Account does not exist'})

        # Check if the debit amount and credit amount are equal
        if float(debit_amount) != float(credit_amount):
            return render(request, 'error.html', {'message': 'Debit and Credit amounts are not equal'})



        # Create the entries instance and save it
        entry = Entries(date=date, description=description, debit_account_id=debit_account,
                        debit_amount=debit_amount, credit_account_id=credit_account,
                        credit_amount=credit_amount)
        entry.save()


        return redirect('success')

    else:
        accounts = Accounts.objects.all()
        return render(request, 'entries.html',{'accounts': accounts}
)

def about(request):
    return render(request,'about.html')


def success(request):
    return render(request, 'success.html')

def owner_capital(request):
     # Get the account IDs for revenues and expenses
     # iexact will match both lowercase and capital case versions of the word.
    revenue_accounts = Accounts.objects.filter(account_type__iexact='revenue').values_list('id', flat=True)
    expense_accounts = Accounts.objects.filter(account_type__iexact='expense').values_list('id', flat=True)
    
    #return a queryset contains debit/credit expenses/revenues and their amount
    debit_expenses = Entries.objects.filter(debit_account_id__account_type='expense').values('debit_account_id__name').annotate(amount=Sum('debit_amount'))
    credit_expenses = Entries.objects.filter(credit_account_id__account_type='expense').values('credit_account_id__name').annotate(amount=Sum('credit_amount'))
    
    debit_revenues = Entries.objects.filter(debit_account_id__account_type='revenue').values('debit_account_id__name').annotate(amount=Sum('debit_amount'))
    credit_revenues = Entries.objects.filter(credit_account_id__account_type='revenue').values('credit_account_id__name').annotate(amount=Sum('credit_amount'))
    # print(credit_revenues)


    # Query the GeneralLedger to get the sum of debit and credit amounts for revenues
    revenue_debit_total = Entries.objects.filter(debit_account_id__in=revenue_accounts).aggregate(Sum('debit_amount'))
    revenue_credit_total = Entries.objects.filter(credit_account_id__in=revenue_accounts).aggregate(Sum('credit_amount'))
    # print(revenue_credit_total)

    revenue_total = abs((revenue_credit_total['credit_amount__sum'] or 0) - (revenue_debit_total['debit_amount__sum'] or 0))
    # If it is None or False, it replaces the value with 0.
    print('revenue_total',revenue_total)

    # Query the GeneralLedger to get the sum of debit and credit amounts for expenses
    expense_debit_total = Entries.objects.filter(debit_account_id__in=expense_accounts).aggregate(Sum('debit_amount'))
    expense_credit_total = Entries.objects.filter(credit_account_id__in=expense_accounts).aggregate(Sum('credit_amount'))
  
    expense_total = abs((expense_credit_total['credit_amount__sum'] or 0) - (expense_debit_total['debit_amount__sum'] or 0))
    print('expense_total',expense_total)
    # Calculate the net income
    net_income = revenue_total - expense_total

    capital_accounts = Accounts.objects.filter(account_type__iexact='equity').values_list('id', flat=True)

      
    debit_capital = Entries.objects.filter(debit_account_id__account_type='equity').annotate(amount=Sum('debit_amount'))
    credit_capital = Entries.objects.filter(credit_account_id__account_type='equity').annotate(amount=Sum('credit_amount'))
    
    capital_debit_total = Entries.objects.filter(debit_account_id__in=capital_accounts).aggregate(Sum('debit_amount'))
    capital_credit_total = Entries.objects.filter(credit_account_id__in=capital_accounts).aggregate(Sum('credit_amount'))
    
    capital_total = abs((capital_credit_total['credit_amount__sum'] or 0) - (capital_debit_total['debit_amount__sum'] or 0))

    drawings_accounts = Accounts.objects.filter(account_type__iexact= 'drawings').values_list('id',flat=True)
       
    debit_drawings = Entries.objects.filter(debit_account_id__account_type='drawings').annotate(amount=Sum('debit_amount'))
    credit_drawings = Entries.objects.filter(credit_account_id__account_type='drawings').annotate(amount=Sum('credit_amount'))
     
    drawings_debit_total = Entries.objects.filter(debit_account_id__in=drawings_accounts).aggregate(Sum('debit_amount'))
    drawings_credit_total = Entries.objects.filter(credit_account_id__in=drawings_accounts).aggregate(Sum('credit_amount'))
    
    drawings_total = abs((drawings_credit_total['credit_amount__sum'] or 0) - (drawings_debit_total['debit_amount__sum'] or 0))
    
    #to avoid negative value we do that
    if(capital_total < 0):
        capital_total = -1 * capital_total
    
    if(drawings_total < 0):
        drawings_total = -1 * drawings_total

    total = net_income + capital_total - drawings_total

    return render(request,'owner_capital.html',{'net_income':net_income,'capital_total':capital_total,'drawings_total':drawings_total,'total':total})

   

def t_account(request):
    accounts = Accounts.objects.all()
    t_accounts = {}
    
    for account in accounts:
        #if account not created it will create it first and initialize debit/credit amount = 0
        if account.name not in t_accounts: 
            t_accounts[account.name] = {'account': account, 'debit_amount': 0, 'credit_amount': 0}
        
        debit_amount = Entries.objects.filter(debit_account_id=account).aggregate(Sum('debit_amount')).get('debit_amount__sum') or 0
        credit_amount = Entries.objects.filter(credit_account_id=account).aggregate(Sum('credit_amount')).get('credit_amount__sum') or 0
        
        t_accounts[account.name]['debit_amount'] += debit_amount
        t_accounts[account.name]['credit_amount'] += credit_amount
    
    return render(request, 't_account.html', {'t_accounts': t_accounts.values()})

def trial_balance(request):
    t_account_list = []
    debits = []
    credits = []
    accounts = Accounts.objects.all()

    for account in accounts:
        debit_amount = Entries.objects.filter(debit_account_id = account).aggregate(Sum('debit_amount')).get('debit_amount__sum') or 0
        credit_amount = Entries.objects.filter(credit_account_id = account).aggregate(Sum('credit_amount')).get('credit_amount__sum') or 0
        debits.append(debit_amount)
        credits.append(credit_amount)
        # print('debits',debits)
        # print(type(debits))
  
        t_account = {
       'account': account,
       'debit_amount': debit_amount,
       'credit_amount': credit_amount
        }

        t_account_list.append(t_account)

    total_debit = sum([debit for debit in debits])
    total_credit = sum([credit for credit in credits])

    # print("total_debit:", total_debit)
    # print("total_credit:", total_credit)
   

    return render(request,'trial_balance.html',{"t_account_list":t_account_list,"total_debit":total_debit,"total_credit":total_credit})

def income_statement(request):

    # Get the account IDs for revenues and expenses
    revenue_accounts = Accounts.objects.filter(account_type__iexact='revenue').values_list('id', flat=True)
    expense_accounts = Accounts.objects.filter(account_type__iexact='expense').values_list('id', flat=True)

    debit_expenses = Entries.objects.filter(debit_account_id__account_type='expense').values('debit_account_id__name').annotate(amount=Sum('debit_amount'))
    credit_expenses = Entries.objects.filter(credit_account_id__account_type='expense').values('credit_account_id__name').annotate(amount=Sum('credit_amount'))
    
    debit_revenues = Entries.objects.filter(debit_account_id__account_type='revenue').values('debit_account_id__name').annotate(amount=Sum('debit_amount'))
    credit_revenues = Entries.objects.filter(credit_account_id__account_type='revenue').values('credit_account_id__name').annotate(amount=Sum('credit_amount'))
   

    # Query the GeneralLedger to get the sum of debit and credit amounts for revenues
    revenue_debit_total = Entries.objects.filter(debit_account_id__in=revenue_accounts).aggregate(Sum('debit_amount'))
    revenue_credit_total = Entries.objects.filter(credit_account_id__in=revenue_accounts).aggregate(Sum('credit_amount'))


    revenue_total = abs((revenue_credit_total['credit_amount__sum'] or 0) - (revenue_debit_total['debit_amount__sum'] or 0))
    # If it is None or False, it replaces the value with 0.

    # Query the GeneralLedger to get the sum of debit and credit amounts for expenses
    expense_debit_total = Entries.objects.filter(debit_account_id__in=expense_accounts).aggregate(Sum('debit_amount'))

    expense_credit_total = Entries.objects.filter(credit_account_id__in=expense_accounts).aggregate(Sum('credit_amount'))
  
    expense_total = (expense_debit_total['debit_amount__sum'] or 0) - (expense_credit_total['credit_amount__sum'] or 0)
   
    # Calculate the net income
    if revenue_total > expense_total:
        net_income = revenue_total - expense_total
    else:
        net_income =  expense_total - revenue_total


# if expense is greater than to make N.I poitive we use a condition.
    # if(net_income < 0):
    #     net_income = -1 * net_income

    income_statement = {
        'debit_expenses': debit_expenses, 
        'credit_expenses': credit_expenses,
        'debit_revenues': debit_revenues,
        'credit_revenues': credit_revenues,
        'revenue_total': revenue_total,
        'expense_total': expense_total,
        'net_income': net_income,
    }

    return render(request,'income_statement.html',{'income_statement':income_statement})

def balance_sheet(request):
    # Get asset accounts
    assets = Accounts.objects.filter(account_type__iexact='asset')

    # Calculate asset balances
    asset_balance = {}
    asset_total = 0
    for asset in assets:
        debit_total = asset.debit_ledger_entries.aggregate(Sum('debit_amount')).get('debit_amount__sum') or 0
        credit_total = asset.credit_ledger_entries.aggregate(Sum('credit_amount')).get('credit_amount__sum') or 0
        balance = debit_total - credit_total
        asset_balance[asset.name] = balance
        asset_total += balance

    # Get liability and equity accounts
    liabilities = Accounts.objects.filter(account_type__iexact='liability')
    equity = Accounts.objects.filter(account_type__iexact='equity')

    # Calculate liability and equity balances
    liability_balance = {}
    equity_balance = {}
    liability_equity_total = 0
    for liability in liabilities:
        debit_total = liability.debit_ledger_entries.aggregate(Sum('debit_amount')).get('debit_amount__sum') or 0
        credit_total = liability.credit_ledger_entries.aggregate(Sum('credit_amount')).get('credit_amount__sum') or 0
        balance = credit_total - debit_total
        liability_balance[liability.name] = balance
        liability_equity_total += balance

    for eq in equity:
        debit_total = eq.debit_ledger_entries.aggregate(Sum('debit_amount')).get('debit_amount__sum') or 0
        credit_total = eq.credit_ledger_entries.aggregate(Sum('credit_amount')).get('credit_amount__sum') or 0
        balance = credit_total - debit_total
        equity_balance[eq.name] = balance
        liability_equity_total += balance

    revenue_accounts = Accounts.objects.filter(account_type__iexact='revenue').values_list('id', flat=True)
    expense_accounts = Accounts.objects.filter(account_type__iexact='expense').values_list('id', flat=True)
    
    #return a queryset contains debit/credit expenses/revenues and their amount
    debit_expenses = Entries.objects.filter(debit_account_id__account_type='expense').values('debit_account_id__name').annotate(amount=Sum('debit_amount'))
    credit_expenses = Entries.objects.filter(credit_account_id__account_type='expense').values('credit_account_id__name').annotate(amount=Sum('credit_amount'))
    
    debit_revenues = Entries.objects.filter(debit_account_id__account_type='revenue').values('debit_account_id__name').annotate(amount=Sum('debit_amount'))
    credit_revenues = Entries.objects.filter(credit_account_id__account_type='revenue').values('credit_account_id__name').annotate(amount=Sum('credit_amount'))
    # print(credit_revenues)


    # Query the GeneralLedger to get the sum of debit and credit amounts for revenues
    revenue_debit_total = Entries.objects.filter(debit_account_id__in=revenue_accounts).aggregate(Sum('debit_amount'))
    revenue_credit_total = Entries.objects.filter(credit_account_id__in=revenue_accounts).aggregate(Sum('credit_amount'))
    # print(revenue_credit_total)

    revenue_total = abs((revenue_credit_total['credit_amount__sum'] or 0) - (revenue_debit_total['debit_amount__sum'] or 0))
    # If it is None or False, it replaces the value with 0.
    print('revenue_total',revenue_total)

    # Query the GeneralLedger to get the sum of debit and credit amounts for expenses
    expense_debit_total = Entries.objects.filter(debit_account_id__in=expense_accounts).aggregate(Sum('debit_amount'))
    expense_credit_total = Entries.objects.filter(credit_account_id__in=expense_accounts).aggregate(Sum('credit_amount'))
  
    expense_total = abs((expense_credit_total['credit_amount__sum'] or 0) - (expense_debit_total['debit_amount__sum'] or 0))
    print('expense_total',expense_total)
    # Calculate the net income
    net_income = revenue_total - expense_total
    print('net_income',net_income)

    
    capital_accounts = Accounts.objects.filter(account_type__iexact='equity').values_list('id', flat=True)

      
    debit_capital = Entries.objects.filter(debit_account_id__account_type='equity').annotate(amount=Sum('debit_amount'))
    credit_capital = Entries.objects.filter(credit_account_id__account_type='equity').annotate(amount=Sum('credit_amount'))
    
    capital_debit_total = Entries.objects.filter(debit_account_id__in=capital_accounts).aggregate(Sum('debit_amount'))
    capital_credit_total = Entries.objects.filter(credit_account_id__in=capital_accounts).aggregate(Sum('credit_amount'))
    
    capital_total = abs((capital_credit_total['credit_amount__sum'] or 0) - (capital_debit_total['debit_amount__sum'] or 0))

    drawings_accounts = Accounts.objects.filter(account_type__iexact= 'drawings').values_list('id',flat=True)
       
    debit_drawings = Entries.objects.filter(debit_account_id__account_type='drawings').annotate(amount=Sum('debit_amount'))
    credit_drawings = Entries.objects.filter(credit_account_id__account_type='drawings').annotate(amount=Sum('credit_amount'))
     
    drawings_debit_total = Entries.objects.filter(debit_account_id__in=drawings_accounts).aggregate(Sum('debit_amount'))
    drawings_credit_total = Entries.objects.filter(credit_account_id__in=drawings_accounts).aggregate(Sum('credit_amount'))
    
    drawings_total = abs((drawings_credit_total['credit_amount__sum'] or 0) - (drawings_debit_total['debit_amount__sum'] or 0))
    
    #to avoid negative value we do that
    if(capital_total < 0):
        capital_total = -1 * capital_total
    
    if(drawings_total < 0):
        drawings_total = -1 * drawings_total

    
    print('capital_total',capital_total)
    equity_balance = net_income + capital_total - drawings_total
    credit_side_total = liability_equity_total + equity_balance

    # Render the balance sheet template with the calculated balances
    return render(request, 'balance_sheet.html', {
        'asset_balance': asset_balance,
        'asset_total': asset_total,
        'liability_balance': liability_balance,
        'equity_balance': equity_balance,
        'liability_equity_total': liability_equity_total,
        'credit_side_total':credit_side_total
    })

