from django import forms
from outgoing import models


class OutgoingForm(forms.ModelForm):

    class Meta:
        model = models.Outgoing
        fields = ['date', 'store', 'description', 'price']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'store': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'date': 'Data',
            'store' : 'Cliente',
            'description': 'Descrição',
            'price': 'Valor',
        }