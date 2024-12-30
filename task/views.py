from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app import metrics
from task import models, forms


class TaskListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10
    permission_required = 'task.view_task'

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get('date')

        if date:
            queryset = queryset.filter(date__icontains=date)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_metrics'] = metrics.get_task_metrics()
        return context
    

class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Task
    template_name = 'task_create.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy('task_list')
    permission_required = 'task.add_task'


class TaskDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Task
    template_name = 'task_detail.html'
    permission_required = 'task.view_task'


class TaskUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Task
    template_name = 'task_update.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy('task_list')
    permission_required = 'task.change_task'


class TaskDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')
    permission_required = 'task.delete_task'
