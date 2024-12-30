from django.urls import path
from . import views

urlpatterns = [
    path('outgoing/list/', views.OutgoingListView.as_view(), name='outgoing_list'),
    path('outgoing/create/', views.OutgoingCreateView.as_view(), name='outgoing_create'),
    path('outgoing/<int:pk>/detail/', views.OutgoingDetailView.as_view(), name='outgoing_detail'),
    path('outgoing/<int:pk>/update/', views.OutgoingUpdateView.as_view(), name='outgoing_update'),
    path('outgoing/<int:pk>/delete/', views.OutgoingDeleteView.as_view(), name='outgoing_delete'),
]
