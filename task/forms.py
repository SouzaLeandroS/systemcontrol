from django import forms
from . import models


class TaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = ['date', 'category', 'status', 'description', 'service_price', 'selling_price', 'adress']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'service_price': forms.TextInput(attrs={'class': 'form-control'}),
            'selling_price': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'date': 'Data',
            'category' : 'Categoria',
            'status': 'Status',
            'description': 'Descrição',
            'service_price': 'Preço',
            'selling_price': 'Preço2',
            'adress': 'Endereço',
        }