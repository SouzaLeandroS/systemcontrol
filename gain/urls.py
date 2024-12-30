from django.urls import path
from gain import views

urlpatterns = [
    path('gain/list/', views.GainListView.as_view(), name='gain_list'),
    path('gain/create/', views.GainCreateView.as_view(), name='gain_create'),
    path('gain/<int:pk>/detail/', views.GainDetailView.as_view(), name='gain_detail'),
    path('gain/<int:pk>/update/', views.GainUpdateView.as_view(), name='gain_update'),
    path('gain/<int:pk>/delete/', views.GainDeleteView.as_view(), name='gain_delete'),
]