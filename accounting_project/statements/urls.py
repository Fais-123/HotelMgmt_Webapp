from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('transaction_form', views.transaction_form, name='transaction_form'),
    path('save_transaction', views.save_transaction, name='save_transaction'),
    path('account_entry', views.account_entry, name='account_entry'),
    path('success', views.success, name='success'),
    path('owner_capital', views.owner_capital, name='owner_capital'),
    path('income_statement',views.income_statement , name='income_statement'),
    path('balance_sheet',views.balance_sheet , name='balance_sheet'),
    

]