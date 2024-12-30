from django.urls import path
from . import views

urlpatterns = [
    path('contract/list/', views.ContractListView.as_view(), name='contract_list'),
    path('contract/create/', views.ContractCreateView.as_view(), name='contract_create'),
    path('contract/<int:pk>/detail/', views.ContractDetailView.as_view(), name='contract_detail'),
    path('contract/<int:pk>/update/', views.ContractUpdateView.as_view(), name='contract_update'),
    path('contract/<int:pk>/delete/', views.ContractDeleteView.as_view(), name='contract_delete'),
]