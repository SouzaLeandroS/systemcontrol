from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app import metrics
from . import models, forms


class GainListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Gain
    template_name = 'gain_list.html'
    context_object_name = 'gains'
    paginate_by = 10
    permission_required = 'gain.view_gain'

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


class GainCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Gain
    template_name = 'gain_create.html'
    form_class = forms.GainForm
    success_url = reverse_lazy('gain_list')
    permission_required = 'gain.add_gain'


class GainDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Gain
    template_name = 'gain_detail.html'
    permission_required = 'gain.view_gain'


class GainUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Gain
    template_name = 'gain_update.html'
    form_class = forms.GainForm
    success_url = reverse_lazy('gain_list')
    permission_required = 'gain.change_gain'


class GainDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Gain
    template_name = 'gain_delete.html'
    success_url = reverse_lazy('gain_list')
    permission_required = 'gain.delete_gain'