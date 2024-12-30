from django import forms
from contract import models


class ContractForm(forms.ModelForm):

    class Meta:
        model = models.Contract
        fields = ['name', 'date_birth', 'cpf', 'rg', 'adress', 'cep', 'mailbox', 'phone', 'service', 'event_date', 'local_pre',
                'event_local', 'total_price', 'input_value', 'input_date', 'residual_value', 'residual_date',]
        widgets = {
            'name': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'date_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'mailbox': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.TextInput(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control'}),
            'local_pre': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'event_local': forms.TextInput(attrs={'class': 'form-control'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'input_value': forms.NumberInput(attrs={'class': 'form-control'}),
            'input_date': forms.DateInput(attrs={'class': 'form-control', 'rows': 3}),
            'residual_value': forms.NumberInput(attrs={'class': 'form-control'}),
            'residual_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome',
            'date_birth': 'Data de Nascimento',
            'cpf' : 'CPF',
            'rg' : 'RG',
            'adress': 'Endereço',
            'cep': 'CEP',
            'maibox': 'E-mail',
            'phone': 'Telefone',
            'service': 'Serviço',
            'event_date': 'Data do Evento',
            'local_pre': 'Local da Prévia',
            'event_local': 'Local do Evento',
            'total_price': 'Valor Total',
            'input_value': 'Valor da Entrada',
            'input_date': 'Data da Entrada',
            'residual_value': 'Valor Restante',
            'residual_date': 'Data Valor Restante',
        }
        referencias = {
            "XXXX": 'name',
            "DATA1": 'date_birth',
            "CCCC": 'cpf',
            "RRRR": 'rg',
            "EEEE": 'adress',
            "PPPP": 'cep',
            "MMMM": 'maibox',
            "TTTT": 'phone',
            "SSSS": 'service',
            "VVVV": 'event_date',
            "LPLP": 'local_pre',
            "LELE": 'event_local',
            "VTVT": 'total_price',
            "VEVE": 'input_value',
            "DTEN": 'input_date',
            "REPG": 'residual_value',
            "DATR": 'residual_date',
            }
        
        

