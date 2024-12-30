from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms
from django.shortcuts import render


class StatusListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Status
    template_name = 'status_list.html'
    context_object_name = 'status'
    permission_required = 'status.view_status'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    

class StatusCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Status
    template_name = 'status_create.html'
    form_class = forms.StatusForm
    success_url = reverse_lazy('status_list')
    permission_required = 'status.add_status'


class StatusDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Status
    template_name = 'status_detail.html'
    permission_required = 'status.view_status'


class StatusUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Status
    template_name = 'status_update.html'
    form_class = forms.StatusForm
    success_url = reverse_lazy('status_list')
    permission_required = 'status.change_status'


class StatusDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Status
    template_name = 'stauts_delete.html'
    success_url = reverse_lazy('status_list')
    permission_required = 'status.delete_status'