from django import forms
from gain import models


class GainForm(forms.ModelForm):

    class Meta:
        model = models.Gain
        fields = ['date', 'customer', 'description', 'price']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'customer': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'date': 'Data',
            'customer' : 'Cliente',
            'description': 'Descrição',
            'price': 'Valor',
        }