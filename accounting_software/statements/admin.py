from django.contrib import admin
from .models import Accounts,Transactions,Entries
# Register your models here.


admin.site.register(Transactions)
admin.site.register(Accounts)
admin.site.register(Entries)