from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app import metrics
from . import models, forms


class OutgoingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Outgoing
    template_name = 'outgoing_list.html'
    context_object_name = 'outgoings'
    paginate_by = 10
    permission_required = 'outgoing.view_outgoing'

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get('date')

        if date:
            queryset = queryset.filter(date__icontains=date)

        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result_metrics'] = metrics.get_result_metrics()
        return context
    

class OutgoingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Outgoing
    template_name = 'outgoing_create.html'
    form_class = forms.OutgoingForm
    success_url = reverse_lazy('outgoing_list')
    permission_required = 'outgoing.add_outgoing'


class OutgoingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Outgoing
    template_name = 'outgoing_detail.html'
    permission_required = 'outgoing.view_outgoing'


class OutgoingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Outgoing
    template_name = 'outgoing_update.html'
    form_class = forms.OutgoingForm
    success_url = reverse_lazy('outgoing_list')
    permission_required = 'outgoing.change_outgoing'


class OutgoingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Outgoing
    template_name = 'outgoing_delete.html'
    success_url = reverse_lazy('outgoing_list')
    permission_required = 'outgoing.delete_outgoing'
