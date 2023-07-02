from django.urls import path
from . import views

urlpatterns = [
    path('',views.income_statement , name='income_statement'),
    path('balance_sheet',views.balance_sheet , name='balance_sheet'),
    # path('logout',views.logout , name='logout'),
]