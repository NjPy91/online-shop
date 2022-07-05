from django.contrib import admin
from .models import *



class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'transaction_type', 'created_time']
    list_filter = ['transaction_type']
    search_fields = ['user__username']





class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance', 'created_time']
    search_fields = ['user__username']


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(UserBalance, UserBalanceAdmin)
