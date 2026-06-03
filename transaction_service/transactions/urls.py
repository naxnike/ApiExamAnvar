from django.urls import path
from .views import TransactionView, StatisticsView

urlpatterns = [
    path('transactions/', TransactionView.as_view(), name='transactions'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]