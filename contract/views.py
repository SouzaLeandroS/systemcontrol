from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class ContractListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Contract
    template_name = 'contract_list.html'
    context_object_name = 'contracts'
    paginate_by = 10
    permission_required = 'contract.view_contract'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    

class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Contract
    template_name = 'contract_create.html'
    form_class = forms.ContractForm
    success_url = reverse_lazy('contract_list')
    permission_required = 'contract.add_contract'


class ContractDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Contract
    template_name = 'contract_detail.html'
    permission_required = 'contract.view_contract'


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Contract
    template_name = 'contract_update.html'
    form_class = forms.ContractForm
    success_url = reverse_lazy('contract_list')
    permission_required = 'contract.change_contract'


class ContractDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Contract
    template_name = 'contract_delete.html'
    success_url = reverse_lazy('contract_list')
    permission_required = 'contract.delete_contract'