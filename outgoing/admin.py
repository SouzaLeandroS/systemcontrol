from django.contrib import admin
from . import models


class OutgoingAdmin(admin.ModelAdmin):
    list_display = ('date', 'store', 'description', 'price',)
    search_fields = ('date',)

admin.site.register(models.Outgoing, OutgoingAdmin)
