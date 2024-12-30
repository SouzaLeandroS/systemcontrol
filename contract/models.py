from django.db import models


class Contract(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    cpf = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    rg = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    adress = models.CharField(max_length=200, null=True, blank=True)
    cep = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    mailbox = models.EmailField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    service = models.TextField(null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    local_pre = models.CharField(max_length=500, null=True, blank=True)
    event_local = models.CharField(max_length=500, null=True, blank=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    input_value = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    input_date = models.DateField(null=True, blank=True)
    residual_value = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    residual_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name