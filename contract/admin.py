from django.contrib import admin
from . import models


class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_birth', 'cpf', 'rg', 'adress', 'mailbox', 'phone', 'service', 'event_date', 'local_pre',
    'event_local', 'total_price', 'input_value', 'input_date', 'residual_value', 'residual_date',)
    search_fields = ('name',)

admin.site.register(models.Contract, ContractAdmin)