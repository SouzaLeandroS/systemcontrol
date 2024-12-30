from django.db import models
from status.models import Status
from categories.models import Category


class Task(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='task')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='task')
    description = models.TextField(null=True, blank=True)
    service_price = models.DecimalField(max_digits=20, decimal_places=2)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    adress = models.CharField(null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return str(self.date)