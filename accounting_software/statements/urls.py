from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name = 'index'),
    path('about',views.about , name = 'about'),
    path('income_statement',views.income_statement, name='income_statement'),
    path('balance_sheet',views.balance_sheet, name='balance_sheet'),
    path('t_account',views.t_account, name='t_account'),
    path('trial_balance',views.trial_balance, name='trial_balance'),
    path('owner_capital',views.owner_capital, name='owner_capital'),
    path('account',views.account, name='account'),
    path('create_transaction',views.create_transaction, name='create_transaction'),
    path('save_entries',views.save_entries, name='save_entries'),
    path('success',views.success, name='success'),

    

]