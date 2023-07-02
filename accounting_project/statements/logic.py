from django.db.models import Sum
from .models import Transaction, Account
from django.db import connection

def generate_owner_capital():
    with connection.cursor() as cur:

        q1 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="service revenue");"""
# q1 service revenue credit amount

        q2 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="service revenue");"""

# q2 service revenue debit amount

        q3 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="tuition revenue");"""

# q3  tuition revenue credit amount
        q4= """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="tuition revenue");"""
# q4 tuition revenue debit amount
        q5 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="Freight revenue");"""
# q5 Freight revenue credit amount
   
        q6 ="""select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="Freight revenue");"""
# q5 Freight revenue debit amount

        q7 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="interest revenue");"""
# q5 interest revenue credit amount

        q8 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="interest revenue");"""
# # q5 interest revenue debit amount

#Expenses
        q9 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="utility expense");"""

        q10 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="utility expense");"""

        q11 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="insurance expense");"""

        q12 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="insurance expense");"""
        
        q13 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="salary expense");"""
        
        q14 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="salary expense");"""
        
        q15 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="rent expense");"""
        
        q16 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="rent expense");"""
        
        q17 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="capital");"""
# q11  capital credit amount

        q18 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="capital");"""
# q12  capital debit amount

        q19 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="drawings");"""
# q12  drawing credit amount

        q20 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="drawings");"""

       
        queries = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]
        result = []
        for query in queries:
            cur.execute(query)
            result1= cur.fetchall()
            result.append(result1)
        print(result)

        values = [float(item[0][0]) for item in result]
       
        service_revenue_credit = values[0]
        service_revenue_debit = values[1]
        print('service_revenue_debit',service_revenue_debit)
        tuition_revenue_credit = values[2]
        tuition_revenue_debit = values[3] 
        freight_revenue_credit = values[4]
        freight_revenue_debit = values[5] 
        interest_revenue_credit = values[6]
        interest_revenue_debit = values[7]
        utility_expense_credit = values[8]
        utility_expense_debit = values[9]
        insurance_expense_credit = values[10]
        insurance_expense_debit = values[11]
        salary_expense_credit = values[12]
        salary_expense_debit = values[13]
        rent_expense_credit = values[14]
        rent_expense_debit = values[15]
        capital_credit = values[16]
        capital_debit = values[17]
        drawings_credit = values[18]
        drawings_debit = values[19]
   
        
        
      
    return service_revenue_credit, service_revenue_debit, tuition_revenue_credit,tuition_revenue_debit,freight_revenue_credit,freight_revenue_debit,interest_revenue_credit,interest_revenue_debit,utility_expense_credit,utility_expense_debit,insurance_expense_credit,insurance_expense_debit,salary_expense_credit,salary_expense_debit,rent_expense_credit,rent_expense_debit,capital_credit,capital_debit,drawings_credit,drawings_debit

def generate_income_statement():
    
    with connection.cursor() as cur:
        
        q1 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="service revenue");"""
# q1 service revenue credit amount

        q2 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="service revenue");"""

# q2 service revenue debit amount

        q3 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="tuition revenue");"""

# q3  tuition revenue credit amount
        
        q4= """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="tuition revenue");"""

# q4 tuition revenue debit amount
        q5 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="Freight revenue");"""
# q5 Freight revenue credit amount
   
        q6 ="""select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="Freight revenue");"""
# q5 Freight revenue debit amount

        q7 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="interest revenue");"""
# q5 interest revenue credit amount

        q8 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="interest revenue");"""
# # q5 interest revenue debit amount

#Expenses
        q9 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="utility expense");"""

        q10 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="utility expense");"""

        q11 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="insurance expense");"""

        q12 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="insurance expense");"""
        
        q13 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="salary expense");"""
        
        q14 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="salary expense");"""
        
        q15 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="rent expense");"""
        
        q16 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="rent expense");"""
        
        
        queries = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16]
        result = []
        for query in queries:
            cur.execute(query)
            result1= cur.fetchall()
            result.append(result1)
        print(result)

        values = [float(item[0][0]) for item in result]
       
        service_revenue_credit = values[0]
        service_revenue_debit = values[1]
        print('service_revenue_debit',service_revenue_debit)
        tuition_revenue_credit = values[2]
        tuition_revenue_debit = values[3] 
        freight_revenue_credit = values[4]
        freight_revenue_debit = values[5] 
        interest_revenue_credit = values[6]
        interest_revenue_debit = values[7]
        utility_expense_credit = values[8]
        utility_expense_debit = values[9]
        insurance_expense_credit = values[10]
        insurance_expense_debit = values[11]
        salary_expense_credit = values[12]
        salary_expense_debit = values[13]
        rent_expense_credit = values[14]
        rent_expense_debit = values[15]
        
      
    return service_revenue_credit, service_revenue_debit, tuition_revenue_credit,tuition_revenue_debit,freight_revenue_credit,freight_revenue_debit,interest_revenue_credit,interest_revenue_debit,utility_expense_credit,utility_expense_debit,insurance_expense_credit,insurance_expense_debit,salary_expense_credit,salary_expense_debit,rent_expense_credit,rent_expense_debit


def generate_balance_sheet():
   
    with connection.cursor() as cur:
        
        q1 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in( select id from statements_account where credit_account="cash");"""

# q1 cash credit amount
        q2= """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="cash");"""
# q2 cash debit amount

        q3 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="land"); """
# q3 land credit amount

        q4 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="land");"""
# q4 land debit amount

        q5 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in( select id from statements_account where credit_account="Property");"""
# q5 property credit amount

        q6 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="Property");"""
# q6 property debit amount

        q7 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="note payable");"""
# q7 note payable credit amount
      
        q8 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="note payable");"""
# q8 note payable debit amount

        q9 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="interest payable");"""
# q9  interest payable credit amount

        q10 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="interest payable");"""
# q10  interest payable credit amount

        q11 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="capital");"""
# q11  capital credit amount

        q12 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="capital");"""
# q12  capital debit amount

        q13 = """select sum(credit_amount) from statements_transaction where statements_transaction.account1_id in(select id from statements_account where credit_account="drawings");"""
# q12  drawing credit amount

        q14 = """select sum(debit_amount) from statements_transaction where statements_transaction.account2_id in(select id from statements_account where debit_account="drawings");"""
# q12  drawing debit amount
  
     
        
        queries = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14]
        result = []
        for query in queries:
            cur.execute(query)
            result1= cur.fetchall()
            result.append(result1)

        values = [float(item[0][0]) for item in result]
      

        cash_credit = values[0]
        cash_debit = values[1]
        land_credit = values[2]
        land_debit = values[3]
        property_credit = values[4]
        property_debit = values[5]
        note_payable_credit =  values[6]
        note_payable_debit  =  values[7]
        interest_payable_credit =  values[8]
        interest_payable_debit  = values[9] 
        capital_credit = values[10]
        capital_debit = values[11]
        drawings_credit = values[12]
        drawings_debit = values[13]
   

    return cash_credit,cash_debit,land_credit,land_debit,property_credit,property_debit,note_payable_credit,note_payable_debit,interest_payable_credit,interest_payable_debit,capital_credit,capital_debit,drawings_credit,drawings_debit
