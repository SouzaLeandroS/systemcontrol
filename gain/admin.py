from django.contrib import admin
from . import models


class GainAdmin(admin.ModelAdmin):
    list_display = ('date', 'customer', 'description', 'price',)
    search_fields = ('date',)

admin.site.register(models.Gain, GainAdmin)