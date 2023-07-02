from django.shortcuts import render,redirect
from .logic import generate_income_statement, generate_balance_sheet,generate_owner_capital
from .models import Transaction,Account
from .forms import TransactionForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def owner_capital(request):
    service_revenue_credit, service_revenue_debit, tuition_revenue_credit,tuition_revenue_debit,freight_revenue_credit,freight_revenue_debit,interest_revenue_credit,interest_revenue_debit,utility_expense_credit,utility_expense_debit,insurance_expense_credit,insurance_expense_debit,salary_expense_credit,salary_expense_debit,rent_expense_credit,rent_expense_debit,capital_credit,capital_debit,drawings_credit,drawings_debit  = generate_owner_capital()
    
    if (service_revenue_credit > service_revenue_debit):
            service_revenue = service_revenue_credit -service_revenue_debit
            print('service_revenue_credit',service_revenue)
    else:
            service_revenue = service_revenue_debit - service_revenue_credit
            print('service_revenue_debit',service_revenue)

    if (tuition_revenue_credit > tuition_revenue_debit):
            tuition_revenue = tuition_revenue_credit -tuition_revenue_debit
            print('tuition_revenue_credit',tuition_revenue)
    else:
            tuition_revenue = tuition_revenue_debit - tuition_revenue_credit
            print('tuition_revenue_debit',tuition_revenue)  

    if (freight_revenue_credit > freight_revenue_debit):
            freight_revenue = freight_revenue_credit -freight_revenue_debit
            print('freight_revenue_credit',freight_revenue)
    else:
            freight_revenue = freight_revenue_debit - freight_revenue_credit
            print('freight_revenue_debit',freight_revenue)

    if (interest_revenue_credit > interest_revenue_debit):
            interest_revenue = interest_revenue_credit -interest_revenue_debit
            print('interest_revenue_credit',interest_revenue)
    else:
            interest_revenue = interest_revenue_debit - interest_revenue_credit
            print('interest_revenue_debit',interest_revenue)

    if (utility_expense_credit > utility_expense_debit):
            utility_expense = utility_expense_credit -utility_expense_debit
            print('utility_expense_credit',utility_expense)
    else:
            utility_expense = utility_expense_debit - utility_expense_credit
            print('utility_expense_debit',utility_expense)

    
    if (insurance_expense_credit > insurance_expense_debit):
            insurance_expense = insurance_expense_credit -insurance_expense_debit
            print('insurance_expense_credit',insurance_expense)
    else:
            insurance_expense = insurance_expense_debit - insurance_expense_credit
            print('insurance_expense_debit',insurance_expense)
    
    if (salary_expense_credit > salary_expense_debit):
            salary_expense = salary_expense_credit -salary_expense_debit
            print('salary_expense_credit',salary_expense)
    else:
            salary_expense = salary_expense_debit - salary_expense_credit
            print('salary_expense_debit',salary_expense)

    if (rent_expense_credit > rent_expense_debit):
            rent_expense = rent_expense_credit - rent_expense_debit
            print('rent_expense_credit', rent_expense)
    else:
            rent_expense = rent_expense_debit - rent_expense_credit
            print('rent_expense_debit', rent_expense)

    if (capital_credit > capital_debit):
            capital = capital_credit - capital_debit
            print('capital_credit',capital)
    else:
            capital = capital_debit - capital_credit
            print('capital_debit',capital)

    if (drawings_credit > drawings_debit):
            drawings = drawings_credit - drawings_debit
            print('drawings_credit',drawings)
    else:
            drawings = drawings_debit - drawings_credit
            print('drawings_debit',drawings)

    revs =  service_revenue + tuition_revenue + freight_revenue + interest_revenue
    exps = utility_expense + insurance_expense + salary_expense + rent_expense
    if revs > exps:
        net_income = revs - exps
    else:
        net_income = exps - revs 

    total = net_income + capital - drawings


    return render(request, 'owner_capital.html', {'net_income': net_income,'capital': capital, 'drawings': drawings,'total':total})

def transaction_form(request):
    form = TransactionForm()
    return render(request, 'transaction_form.html', {'form': form})

def save_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            #form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = TransactionForm()
    
    return render(request, 'transaction_form.html', {'form': form})

    

def account_entry(request):
    if request.method == 'POST':
        credit_account = request.POST.get('credit_account')
        debit_account = request.POST.get('debit_account')
        account_type = request.POST.get('account_type')

        # Perform any required validation or saving logic here

        if not credit_account or not debit_account or not account_type:
            return redirect('account_form.html')  # Redirect back to the form if there are validation errors

        # Save the form data to the database
        account = Account(credit_account=credit_account, debit_account=debit_account, account_type=account_type)
        account.save()

        return redirect('success')

    return render(request, 'account_form.html')




def success(request):
    return render(request, 'success.html')


def income_statement(request):
    service_revenue_credit, service_revenue_debit, tuition_revenue_credit,tuition_revenue_debit,freight_revenue_credit,freight_revenue_debit,interest_revenue_credit,interest_revenue_debit,utility_expense_credit,utility_expense_debit,insurance_expense_credit,insurance_expense_debit,salary_expense_credit,salary_expense_debit,rent_expense_credit,rent_expense_debit = generate_income_statement()
    
    if (service_revenue_credit > service_revenue_debit):
            service_revenue = service_revenue_credit -service_revenue_debit
            print('service_revenue_credit',service_revenue)
    else:
            service_revenue = service_revenue_debit - service_revenue_credit
            print('service_revenue_debit',service_revenue)

    if (tuition_revenue_credit > tuition_revenue_debit):
            tuition_revenue = tuition_revenue_credit -tuition_revenue_debit
            print('tuition_revenue_credit',tuition_revenue)
    else:
            tuition_revenue = tuition_revenue_debit - tuition_revenue_credit
            print('tuition_revenue_debit',tuition_revenue)  

    if (freight_revenue_credit > freight_revenue_debit):
            freight_revenue = freight_revenue_credit -freight_revenue_debit
            print('freight_revenue_credit',freight_revenue)
    else:
            freight_revenue = freight_revenue_debit - freight_revenue_credit
            print('freight_revenue_debit',freight_revenue)

    if (interest_revenue_credit > interest_revenue_debit):
            interest_revenue = interest_revenue_credit -interest_revenue_debit
            print('interest_revenue_credit',interest_revenue)
    else:
            interest_revenue = interest_revenue_debit - interest_revenue_credit
            print('interest_revenue_debit',interest_revenue)

    if (utility_expense_credit > utility_expense_debit):
            utility_expense = utility_expense_credit -utility_expense_debit
            print('utility_expense_credit',utility_expense)
    else:
            utility_expense = utility_expense_debit - utility_expense_credit
            print('utility_expense_debit',utility_expense)

    
    if (insurance_expense_credit > insurance_expense_debit):
            insurance_expense = insurance_expense_credit -insurance_expense_debit
            print('insurance_expense_credit',insurance_expense)
    else:
            insurance_expense = insurance_expense_debit - insurance_expense_credit
            print('insurance_expense_debit',insurance_expense)
    
    if (salary_expense_credit > salary_expense_debit):
            salary_expense = salary_expense_credit -salary_expense_debit
            print('salary_expense_credit',salary_expense)
    else:
            salary_expense = salary_expense_debit - salary_expense_credit
            print('salary_expense_debit',salary_expense)

    if (rent_expense_credit > rent_expense_debit):
            rent_expense = rent_expense_credit - rent_expense_debit
            print('rent_expense_credit', rent_expense)
    else:
            rent_expense = rent_expense_debit - rent_expense_credit
            print('rent_expense_debit', rent_expense)

    revs =  service_revenue + tuition_revenue + freight_revenue + interest_revenue
    exps = utility_expense + insurance_expense + salary_expense + rent_expense
    net_income = revs - exps

    revenues = {
        'service revenue': service_revenue,
        'tuition_revenue': tuition_revenue,
        'freight_revenue': freight_revenue,
        'interest_revenue': interest_revenue,
        'total': revs
    }

    expenses = {
         'utility expense': utility_expense,
         'insurance_expense': insurance_expense,
         'salary_expense': salary_expense,
         'rent_expense': rent_expense,
         'total': exps
    }

    return render(request, 'income_statement.html', {'revenues': revenues, 'expenses': expenses, 'net_income': net_income})


def balance_sheet(request):
        
        cash_credit, cash_debit, land_credit, land_debit, property_credit, property_debit,note_payable_credit,note_payable_debit,interest_payable_credit,interest_payable_debit,capital_credit,capital_debit,drawings_credit,drawings_debit = generate_balance_sheet()

        if (cash_credit > cash_debit):
            cash = cash_credit -cash_debit
            print('cash_credit',cash)
        else:
            cash = cash_debit - cash_credit
            print('cash_debit',cash)

        if (land_credit > land_debit):
            land = land_credit -land_debit
            print('land_credit',land)
        else:
            land = land_debit - land_credit
            print('land_debit',land)  

        if (property_credit > property_debit):
            property = property_credit - property_debit
            print('property_credit',property)
        else:
            property = property_debit - property_credit
            print('property_debit',property)

        if (note_payable_credit > note_payable_debit):
            note_payable = note_payable_credit - note_payable_debit
            print('note_payable_credit',note_payable)
        else:
            note_payable = note_payable_debit - note_payable_credit
            print('note_payable_debit',note_payable)

        if (interest_payable_credit > interest_payable_debit):
            interest_payable = interest_payable_credit - interest_payable_debit
            print('interest_payable_credit',interest_payable)
        else:
            interest_payable = interest_payable_debit - interest_payable_credit
            print('interest_payable_debit',interest_payable)

        if (capital_credit > capital_debit):
            capital = capital_credit - capital_debit
            print('capital_credit',capital)
        else:
            capital = capital_debit - capital_credit
            print('capital_debit',capital)

        if (drawings_credit > drawings_debit):
            drawings = drawings_credit - drawings_debit
            print('drawings_credit',drawings)
        else:
            drawings = drawings_debit - drawings_credit
            print('drawings_debit',drawings)
            
        total = cash + land + property

        total =  note_payable + interest_payable + capital - drawings

        asset_balances = {
        'Cash': cash,
        'Land': land,
        'Property': property,
        'total': total
    }

        liability_equity_balances = {
        'note_payable': note_payable,
        'interest_payable': interest_payable,
        'capital': capital,
        'drawings': drawings,
        'total': total
            }

        return render(request, 'balance_sheet.html', {
        'asset_balances': asset_balances,
        'liability_equity_balances': liability_equity_balances,
    })
