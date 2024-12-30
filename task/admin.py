from django.contrib import admin
from . import models


class TaskAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'status', 'description', 'service_price', 'selling_price', 'adress',)
    search_fields = ('date',)

admin.site.register(models.Task, TaskAdmin)