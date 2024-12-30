from django.contrib import admin
from . import models


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)

admin.site.register(models.Status, StatusAdmin)
